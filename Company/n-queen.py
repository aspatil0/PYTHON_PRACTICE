N = 8

def print_solution(board):
    for row in board:
        print(row)

def is_safe(board, row, col):
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

def solve(board, col):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve(board, col + 1):
                return True
            board[i][col] = 0
    return False

board = [[0 for _ in range(N)] for _ in range(N)]
board[0][0] = 1

if solve(board, 1):
    print_solution(board)
else:
    print("No solution exists")
