from rkode.game_base_module import GameBase

class Sudoku(GameBase):
    def find_next_empty(self, puzzle):
        for row in range(len(puzzle)):
            for col in range(len(puzzle)):
                if puzzle[row][col] == -1:
                    return row, col
                
        return None, None

    def is_valid(self, puzzle, guess, row, col):
        row_vals = puzzle[row]
        if guess in row_vals:
            return False

        col_vals = [puzzle[i][col] for i in range(9)]
        if guess in col_vals:
            return False
        
        row_start = (row//3) * 3
        col_start = (col//3) * 3

        for l_row in range(row_start, row_start + 3):
            for l_col in range(col_start, col_start + 3):
                if puzzle[l_row][l_col] == guess:
                    return False

        return True

    def solve_sudoku(self, puzzle):
        row, col = self.find_next_empty(puzzle)

        if row is None:
            return True
        
        for guess in range(1, 10):
            if self.is_valid(puzzle, guess, row, col):
                puzzle[row][col] = guess

                if self.solve_sudoku(puzzle):
                    return True
            puzzle[row][col] == -1

        return False
    
# pass list of list to solvesudoku