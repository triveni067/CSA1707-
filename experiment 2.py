# 8-Queen Problem (Single Solution)

N = 8  # size of the chessboard

def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False

    return True

def solve(board, row):
    if row >= N:
        print_solution(board)
        return True  # Stop after first solution

    for i in range(N):
        if is_safe(board, row, i):
            board[row][i] = True
            if solve(board, row + 1):
                return True
            board[row][i] = False
    return False

def eight_queen():
    board = [[False] * N for _ in range(N)]
    if not solve(board, 0):
        print("No solution exists")

eight_queen()
