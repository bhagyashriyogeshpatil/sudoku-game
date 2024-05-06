
class Board:
    """
    Represents a Sudoku board.
    """
    def __init__(self, board):
        """
        Initializes a Sudoku board.
        """       
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
        """
        Find the first empty cell in the Sudoku board.

        Returns:
            tuple or None: A tuple containing the row and column indices of the first empty cell,
                or None if no empty cell is found.
        """
        for row in range(len(self.board)):
            try:
                col = self.board[row].index(0)
                return row, col
            # Handle the ValueError exception that is thrown if 0 is not found
            except ValueError:
                pass
        return None

    def confirm_valid(self, empty, num):
        """
        Check if placing a number in a specific cell is valid.

        Args:
            empty (tuple): A tuple containing the row and column indices of the cell.
            num (int): The number to be placed in the cell.

        Returns:
            bool: True if placing the number is valid, False otherwise.
        """
        row, col = empty
        return (
            self.valid_in_row(row, num) and
            self.valid_in_col(col, num) and
            self.valid_in_square(row, col, num)
        )

    def valid_in_row(self, row, num):
        """
        Check if a number is valid in a specific row.
        Args:
            row (int): The row index.
            num (int): The number to be checked.

        Returns:
            bool: True if the number is not present in the row, False otherwise.
        """
        row_values = self.board[row]
        return num not in row_values

    def valid_in_col(self, col, num): 
        """
        Check if a number is valid in a specific column.

        Args:
            col (int): The column index.
            num (int): The number to be checked.

        Returns:
            bool: True if the number is not present in the column, False otherwise.
        """ 
        for row in range(len(self.board)):
            if self.board[row][col] == num:
                return False
        return True 

    def valid_in_square(self, row, col, num):
        """
        Check if a number is valid in a specific 3x3 square.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            num (int): The number to be checked.

        Returns:
            bool: True if the number is not present in the square, False otherwise.
        """
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def solve_sudoku(self):
        """
        Solves a Sudoku puzzle recursively using backtracking algorithm.

        Returns:
            bool: True if the puzzle is solved successfully, False otherwise.
        """
        empty_cell = self.find_empty_cell()

        # If no empty cell is found, the puzzle is solved
        if empty_cell is None:
            return True

        row, col = empty_cell

        # Try placing numbers 1 to 9 in the empty cell
        for guess in range(1, 10):
            
            # Check if the guessed number is valid
            if self.confirm_valid((row, col), guess):
                # Place the guessed number in the empty cell
                self.board[row][col] = guess
                
                # Recursively try solving the puzzle with the guessed number
                if self.solve_sudoku():
                    return True
                
                # If the guess leads to a dead end, backtrack
                self.board[row][col] = 0
                
        # If no number can be placed in the empty cell, backtrack
        return False

    def play_sudoku(self):
        """
        Allows users to play Sudoku interactively by entering their guesses for empty cells.
        """
        while True:
            row = input("Enter the row to insert number (1-9) or 'q' to quit/solved puzzle: ")
            if row.lower() == 'q':
                print("Quitting the game.")
                break
            col = input("Enter the column to insert number (1-9) or 'q' to quit/solved puzzle: ")
            if col.lower() == 'q':
                print("Quitting the game.")
                break
            num = input("Enter a number (1-9) or 'q' to quit/solved puzzle: ")
            if num.lower() == 'q':
                print("Quitting the game.")
                break

            # Convert inputs to integers
            try:
                row = int(row) - 1
                print("row:", row)
                col = int(col) - 1
                print("col:", col)
                num = int(num)
                print("num:", num)
            except ValueError:
                print("Invalid input. Please enter numbers between 1 and 9.")
                continue

            # Check if the entered number is valid
            if not (1 <= num <= 9):
                print("Invalid input. Please enter numbers between 1 and 9.")
                continue

            # Check if the entered cell is empty
            if self.board[row][col] != 0:
                print("Cell value: ", self.board[row][col])
                print("This cell is already filled. Try another one.")
                continue

            # Check if the guessed number is valid
            valid_num = self.confirm_valid((row, col), num)
            print("valid_num: ", valid_num)
            if not self.confirm_valid((row, col), num):
                print("Invalid number. Try again.")
                continue
            

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
    print("\nLet's play Sudoku!\n")
    gameboard.play_sudoku()
    if gameboard.solve_sudoku():
        print('\nSolved puzzle:')
        gameboard.print_board()    
    else:
        print('\nThe provided puzzle is unsolvable.')

if __name__=="__main__":
    main()