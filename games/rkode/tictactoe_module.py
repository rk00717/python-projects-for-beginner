from abc import ABC, abstractmethod
from random import choice
from time import sleep
from os import system
from math import inf

from rkode.game_base_module import GameBase

class PlayerBase(ABC):
    def __init__(self, letter):
        self.letter = letter
        
    @abstractmethod
    def get_move(self, game):
        ...

class DumbComputer(PlayerBase):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if not game.debug_mode:
            print(f"{self.letter} is thinking!!!")
            sleep(3)
        spot = choice(game.available_moves())
        return spot

class SmartComputer(PlayerBase):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if not game.debug_mode:
            print(f"{self.letter} is thinking!!!")
            sleep(3)
        if len(game.available_moves()) == 9:
            spot = choice(game.available_moves())
        else:
            spot = self.min_max(game, self.letter)["position"]

        return spot

    def min_max(self, state, player):
        max_player = self.letter
        min_player = 'O' if player == 'X' else 'X'

        if state.winner == min_player:
            spot_count = state.get_empty_spot + 1
            return {
                "position" : None,
                "score" : 1 * spot_count if min_player == max_player else -1 * spot_count
            }
        elif not state.is_empty_spot_available:
            return { "position" : None, "score" : 0}
        
        if player == max_player:
            best_score = { "position" : None, "score" : -inf}
        else:
            best_score = { "position" : None, "score" : inf}

        # Finding possible move
        for possible_move in state.available_moves():
            # making move
            state.make_move(possible_move, player)
            
            # recurse the process
            simulated_score = self.min_max(state, min_player)
            
            # undo the move
            state.board[possible_move] = ' '
            state.winner = None
            simulated_score["position"] = possible_move
            
            # update result if necessary
            if player == max_player:
                if simulated_score["score"] > best_score["score"]:
                    best_score = simulated_score
            else:
                if simulated_score["score"] < best_score["score"]:
                    best_score = simulated_score

        return best_score

class User(PlayerBase):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_spot = False
        spot = None
        while not valid_spot:
            spot = input(f"{self.letter}'s turn. \nEnter your Move[0-8] : ")
            if spot.isdigit:
                spot = int(spot)
                if spot in game.available_moves():
                    valid_spot = True
                    break
                else:
                    print("Invalid spot. Try again.")
            else:
                print("Move should be a number.")

        return spot

class Board:
    debug_mode = True

    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def display_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def display_board_nums():
        print("\nReference Board -> ")
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def is_player_won(self, spot, player_symbol):
        row_index = spot//3
        row = self.board[row_index*3 : (row_index + 1) *3]

        col_index = spot%3
        col = [self.board[col_index+i*3] for i in range(3)]

        row_res = [square == player_symbol for square in row]
        col_res = [square == player_symbol for square in col]

        if all(row_res) or all(col_res):
            return True
        
        if spot%2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]

            diag_1_res = [square == player_symbol for square in diagonal_1]
            diag_2_res = [square == player_symbol for square in diagonal_2]

            if all(diag_1_res) or all(diag_2_res):
                return True

        return False

    def make_move(self, spot, player_symbol):
        self.board[spot] = player_symbol
        if self.is_player_won(spot, player_symbol):
            self.winner = player_symbol

    @property
    def is_empty_spot_available(self):
        return ' ' in self.board
    
    @property
    def get_empty_spot(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def display_result(self, message):
        if self.debug_mode:
            return
        
        system("cls")
        print(f"\n{message}")
        print("")
        self.display_board()
        print("")
        system("pause")


class TicTacToe(GameBase):
    def ask(self, question):
        preference = input(f"{question} [Y/N] : ").lower()
        if preference == "y":
            return True
        
        return False

    def take_player(self, player_symbol):
        if self.ask(f"Do you want to have player {player_symbol} as Human?"):
            return User(player_symbol)

        if self.ask("Do you want me to play smart?"):
            return SmartComputer(player_symbol)
        
        return DumbComputer(player_symbol)

    def play(self, game, player1, player2, debug_mode = False):
        IsXTurn = True
        game.debug_mode = debug_mode

        while game.is_empty_spot_available:
            if not game.debug_mode:
                system("cls")
                print("You are playing -> Tic Tac Toe\n")
                game.display_board_nums()

            print("")
            game.display_board()
            print("")

            spot = player1.get_move(game) if IsXTurn else player2.get_move(game)

            player_symbol = 'X' if IsXTurn else 'O'

            game.make_move(spot, player_symbol)
            
            print(f"\n{player_symbol}'s made move to spot {spot}")

            IsXTurn = not IsXTurn

            if game.winner:
                game.display_result(f"{game.winner} won the game")
                break
            elif game.get_empty_spot == 0:
                game.display_result("Match Draw...")
                break

            if not game.debug_mode:
                sleep(1)

    def debug_play(self):
        xwin = 0
        owin = 0
        draw = 0
        iterations = 1000
        for _ in range(iterations):
            print(f"ITERATION => {_}")
            xP = SmartComputer('X')
            oP = SmartComputer('O')
            t = Board()
            result = self.play(t, xP, oP, True)
            if result == 'X':
                xwin += 1
            elif result == 'O':
                owin += 1
            else:
                draw += 1
            print(f"After {_}, The results are : \n{xwin} wins, {owin} wins, and {draw} draw")

        # print(f"After {iterations}, The results are : \n{xwin} wins, {owin} wins, and {draw} draw")
        system("pause")

    def start_game(self):
        system("cls")
        print("You are playing -> Tic Tac Toe\n")
        
        # self.debug_play()
        player_1 = self.take_player('X')
        player_2 = self.take_player('O')
        game = Board()
        self.play(game, player_1, player_2)