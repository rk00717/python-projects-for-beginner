from rkode.game_base_module import GameBase

from random import randint
from os import system

class Board:
    def __init__(self, board_size, bomb_count):
        self.board_size = board_size
        self.bomb_count = bomb_count

        self.board = self.make_new_board()
        self.setup_weight_to_board()

        self.dug_spot = set()

    def make_new_board(self):
        board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

        plantation_count = 0
        while plantation_count < self.bomb_count:
            location = randint(0, self.board_size**2 - 1)
            row = location // self.board_size
            col = location % self.board_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            plantation_count += 1

        return board
    
    def setup_weight_to_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == '*':
                    continue
                self.board[row][col] = self.get_neighbouring_bombs_count(row, col)
    
    def get_neighbouring_bombs_count(self, row, col):
        bomb_count = 0
        for grid_row in range(max(0, row-1), min(self.board_size, row+2)):
            for grid_col in range(max(0, col-1), min(self.board_size, col+2)):
                if grid_row == row and grid_col == col:
                    continue
                if self.board[grid_row][grid_col] == '*':
                    bomb_count += 1

        return bomb_count
    
    def dig_at_location(self, row, col):
        self.dug_spot.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        for grid_row in range(max(0, row-1), min(self.board_size-1, row+2)):
            for grid_col in range(max(0, col-1), min(self.board_size-1, col+2)):
                if (grid_row, grid_col) in self.dug_spot:
                    continue

                self.dig_at_location(grid_row, grid_col)

        return True

    def __str__(self):
        header = '    ' + '   '.join(str(i) for i in range(self.board_size))
        separator = '  ' + '--' * (2 * self.board_size)

        rows = "\n".join([f'{i} | ' + ' | '.join(str(self.board[i][j] if (i, j) in self.dug_spot else ' ') for j in range(self.board_size))+ ' |' for i in range(self.board_size)])
        result = f"\n{header}\n{separator}\n{rows}\n{separator}"
        
        return result


class Minesweeper(GameBase):
    def play(self, board_size = 10, bomb_count = 10):
        board = Board(board_size, bomb_count)


        did_successfully_dug = True
        while len(board.dug_spot) < board.board_size**2 - bomb_count:
            system("cls")
            print("You are playing -> Minesweeper 💣\n")
            print(board)

            dig_location = input("Where to Dig? [Row, Column] : ")
            row, col = map(int, dig_location.split(','))
            if (row < 0 or row >= board.board_size or col < 0 or col >= board.board_size):
                print("Invalid dig location. Try Again!!!")
                continue

            did_successfully_dug = board.dig_at_location(row, col)
            if not did_successfully_dug:
                system("cls")
                print("Rest in peace, buddy...")
                break

        if did_successfully_dug:
            system("cls")
            print("Congrats Miner!!! You Did it great.")
        else:
            # print("Game Over Miner... :(")
            board.dug_spot = [(row, col) for row in range(board.board_size) for col in range(board.board_size)]
            
        print(board)

    def start_game(self):
        super().start_game()
        system("cls")
        self.play(5,5)
        system("pause")