#!/usr/bin/env python3
"""N-queens puzzle
   auth: EDOGUN PETER UYI
"""

import sys


def is_valid(board, row, col):
    """Check if a queen can be placed on board at (row, col)."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """Solve the N Queens problem and print all solutions."""
    def solve(board, row):
        if row == n:
            print([[i, board[i]] for i in range(n)])
            return

        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    board = [-1] * n
    solve(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)

