"""1. Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens
according to the following constraints.
a. Each row should have exactly only one queen.
b. Each column should have exactly only one queen.
c. No queens are attacking each other."""

import random

def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def random_place_queens(n):
    while True:
        board = [-1] * n
        for row in range(n):
            possible_positions = [col for col in range(n) if is_safe(board, row, col)]
            if not possible_positions:
                break
            board[row] = random.choice(possible_positions)

        if -1 not in board:  # If all queens are placed successfully
            return board

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ["Q" if col == board[row] else "." for col in range(n)]
        print(" ".join(line))
    print()


n = 8  # Chessboard size (8x8)
solution = random_place_queens(n)
print("Random placement of queens:")
print_board(solution)