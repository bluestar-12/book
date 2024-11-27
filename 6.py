def is_safe(board, row, col, N):
    
    for i in range(col):
        if board[row][i] == 1:
            return False
    
   
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
   
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queen(board, col, N):
    
    if col >= N:
        return True
    
   
    for i in range(N):
        if is_safe(board, i, col, N):
            
            board[i][col] = 1
            
            
            if solve_n_queen(board, col + 1, N):
                return True
            
           
            board[i][col] = 0
    
    return False

def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()

def solve_n_queens(N):
   
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    
    if not solve_n_queen(board, 0, N):
        print(f"No solution exists for {N} queens.")
        return
    
   
    print(f"Solution for {N} queens:")
    print_solution(board, N)


try:
    N = int(input("Enter the number of queens (N): "))
    if N <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        solve_n_queens(N)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
