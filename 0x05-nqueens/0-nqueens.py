#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    """
    Check if placing a queen at position (row, col) is valid.
    """
    # Check row and column
    for i in range(len(board)):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    # Check diagonals
    for i in range(len(board)):
        for j in range(len(board)):
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == 1:
                    return False

    return True

def solve_nqueens(board, col):
    """
    Recursive function to solve the N queens problem.
    """
    if col >= len(board):
        print_solution(board)
        return True

    res = False
    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1) or res
            board[i][col] = 0

    return res

def print_solution(board):
    """
    Print the solution board.
    """
    queens = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                queens.append([i, j])
    print(queens)

def nqueens(N):
    """
    Main function to solve the N queens problem.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
