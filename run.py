
class Board:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        """
        Print the Sudoku board in format so it is readable.
        This method prints the Sudoku board in a visually formatted manner,
        separating rows and columns with '|' and adding horizontal dividers
        after every third row.
        """
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if col == 0:
                    print(" | ", end='')
                if col != 8:
                    print(self.board[row][col], end=' ')
                else:
                    print(self.board[row][col], end='')
                if (col + 1) % 3 == 0:
                    print(" | ", end='')
            if (row + 1) % 3 == 0:
                print("\n-----------------------------", end='')
            print()

    def find_empty_cell(self):
        for row in range(len(self.board)):
            try:
                col = self.board[row].index(0)
                print("Tuple: ", row, col)
                return row, col
            # Handle the ValueError exception that is thrown if 0 is not found
            except ValueError:
                pass
        return None

    def confirm_valid(self, empty, num):
        pass

    def solve_sudoku(self):
        """
         Solves a Sudoku puzzle recursively using backtracking algorithm.
        """
        empty_cell = self.find_empty_cell()
        print("Empty cell", empty_cell)

        # If no empty cell is found, the puzzle is solved
        if empty_cell is None:
            return True

        row, col = empty_cell

        # Try placing numbers 1 to 9 in the empty cell
        for guess in range(1, 10):
            print("Guess: ", guess)
            # Check if the guessed number is valid
            if self.confirm_valid((row, col), guess):
                # Place the guessed number in the empty cell
                print("Guess Placed: ", self.board[row][col])
                self.board[row][col] = guess
                
                # Recursively try solving the puzzle with the guessed number
                if self.solve_sudoku():
                    return True
                
                # If the guess leads to a dead end, backtrack
                self.board[row][col] = 0
                
        # If no number can be placed in the empty cell, backtrack
        return False


def main():
    print("Welcome to Sudoku Game")
    puzzle = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]
    gameboard = Board(puzzle)
    print('Puzzle to solve:')
    gameboard.print_board()
    gameboard.solve_sudoku()

if __name__=="__main__":
    main()