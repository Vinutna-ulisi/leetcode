def print_solution(board): 
    for row in board: 
        print(" ".join('Q' if col else '.' for col in row)) 
    print() 
 
def is_safe(board, row, col, n): 
    for i in range(row): 
        if board[i][col] :
           (col - row + i >= 0 and board[i][col - row + i]) 
           (col + row - i < n and board[i][col + row - i]) 
        return False 
    return True 
 
def solve_n_queens(board, row, n): 
    if row == n: 
        print_solution(board) 
        return True 
    res = False 
    for col in range(n): 
        if is_safe(board, row, col, n): 
            board[row][col] = 1 
            res = solve_n_queens(board, row + 1, n) or res 
            board[row][col] = 0 
    return res 
n = 4 
board = [[0]*n for _ in range(n)] 
solve_n_queens(board, 0, n)
