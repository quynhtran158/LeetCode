'''
kho' vl wtf
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int):
            # When the row number equals 'n', it means all queens are placed successfully
            if row == n:
                # Save a solution by converting each row's list representation to a string
                solution.append([''.join(row_state) for row_state in board])
                return
            # Iterate over columns to try placing a queen
            for col in range(n):
                # Check if placing a queen here violates no constraints
                if column[col] + diagonal[row + col] + anti_diagonal[n - row + col] == 0:
                    # Place the queen by updating the board and marking the corresponding constraints
                    board[row][col] = "Q"
                    column[col] = diagonal[row + col] = anti_diagonal[n - row + col] = 1
                    # Move on to the next row
                    backtrack(row + 1)
                    # Backtrack: remove the queen and the constraints
                    column[col] = diagonal[row + col] = anti_diagonal[n - row + col] = 0
                    board[row][col] = "."

        # Initialize solution list
        solution = []
        # Initialize board with dots representing empty spaces
        board = [["."] * n for _ in range(n)]
        # Prepare constraint lists to check the columns and diagonals/anti-diagonals
        column = [0] * n
        diagonal = [0] * (2 * n)
        anti_diagonal = [0] * (2 * n)
        # Start the backtracking algorithm from the first row
        backtrack(0)
        # Return the list of all the solutions after converting them to the expected output format
        return solution