def is_safe(board, row, col, N):
    # Check the current column on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queen(board, col, N):
    # If all queens are placed
    if col >= N:
        return True
    
    # Try placing the queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen
            board[i][col] = 1
            
            # Recur to place the rest of the queens
            if solve_n_queen(board, col + 1, N):
                return True
            
            # If placing queen in board[i][col] doesn't lead to a solution, remove queen (backtrack)
            board[i][col] = 0
    
    return False

def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()

def solve_n_queens(N):
    # Initialize the board with 0s
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    # Start solving the N-Queen problem
    if not solve_n_queen(board, 0, N):
        print(f"No solution exists for {N} queens.")
        return
    
    # Print the solution
    print(f"Solution for {N} queens:")
    print_solution(board, N)

# Input from the user
try:
    N = int(input("Enter the number of queens (N): "))
    if N <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        solve_n_queens(N)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
