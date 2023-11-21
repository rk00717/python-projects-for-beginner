from abc import ABC, abstractmethod
from random import choice
from time import sleep
from os import system

from rkode.game_base_module import GameBase

class PlayerBase(ABC):
    def __init__(self, letter):
        self.letter = letter
        
    @abstractmethod
    def get_move(self, game):
        ...

class Computer(PlayerBase):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        spot = choice(game.available_moves())
        return spot

class User(PlayerBase):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_spot = False
        spot = None
        while not valid_spot:
            spot = input(f"{self.letter}'\'s turn. \nEnter your Move[1-9] : ")
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
    def get_spot_count(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def display_result(self, message):
        system("cls")
        print(f"\n{message}")
        print("")
        self.display_board()
        print("")
        system("pause")

    def play(self, player1, player2):
        IsXTurn = True
        while self.is_empty_spot_available:
            system("cls")
            print("You are playing -> Tic Tac Toe\n")
            self.display_board_nums()
            print("")
            self.display_board()
            print("")

            spot = player1.get_move(self) if IsXTurn else player2.get_move(self)

            player_symbol = 'X' if IsXTurn else 'O'

            self.make_move(spot, player_symbol)
            
            print(f"\n{player_symbol}'s made move to spot {spot}")

            IsXTurn = not IsXTurn

            if self.winner:
                self.display_result(f"{self.winner} won the game")
                break
            elif self.get_spot_count == 0:
                self.display_result("Match Draw...")
                break

            sleep(1)


class TicTacToe(GameBase):
    def start_game(self):
        player_1 = User('X')
        player_2 = User('O')
        # player_1 = Computer('X')
        # player_2 = Computer('O')
        game = Board()
        game.play(player_1, player_2)