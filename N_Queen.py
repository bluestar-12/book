class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        
    def printBoard(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    print(" Q ", end="")
                else:
                    print(" - ", end="")
            print("\n")

    def check_safe(self, row_index, col_index):
        # Check horizontally
        for i in range(self.n):
            if self.board[row_index][i] == 1:
                return False
    
        # Check vertically from top left to right bottom
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.board[i][j] == 1:
                return False
            j = j - 1
        
        # Check diagonally from right top to left bottom 
        j = col_index
        for i in range(row_index, self.n):
            if i < 0:
                break
            if self.board[i][j] == 1:
                return False
            j = j - 1

        return True
    
    def solve(self, col_index):
        if col_index == self.n:
            return True
       
        for row_index in range(self.n):
            if self.check_safe(row_index, col_index):
                self.board[row_index][col_index] = 1
                if self.solve(col_index + 1):
                    return True
                self.board[row_index][col_index] = 0
        return False
    
    def solve_NQueens(self):
        if self.solve(0):
            self.printBoard()
        else:
            print("No possible solution")     

# Function to get user input for the N-Queens problem
def get_user_input():
    n = int(input("Enter the value of N (size of the board): "))
    queens = NQueens(n)
    queens.solve_NQueens()

# Call the function to get user input and solve the N-Queens problem
get_user_input()

# Time Complexity:
# The time complexity for solving the N-Queens problem using backtracking is O(N!). 
# This is because for each column, you try placing queens in all possible rows, 
# and there are N columns, leading to an O(N!) complexity in the worst case.

# Space Complexity:
# The space complexity is O(N^2) because of the NxN board that is used to store 
# the positions of the queens and the recursive stack space used by the backtracking algorithm.
