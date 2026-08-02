# Battleship — Python starter
# Run: python3 battleship.py

import random

SIZE = 5
SHIP_LENGTH = 3


def make_board():
    # board[row][col]: "." = unknown, "X" = hit, "O" = miss
    return [["." for _ in range(SIZE)] for _ in range(SIZE)]


def print_board(board):
    print("  " + " ".join(str(c) for c in range(SIZE)))
    for r, row in enumerate(board):
        print(f"{r} " + " ".join(row))


def place_ship():
    # MILESTONE 2: return the ship's cells as a list of (row, col) tuples —
    # SHIP_LENGTH cells in a line (horizontal or vertical), random position,
    # fully inside the board.
    # TODO
    return []


def main():
    board = make_board()
    ship = place_ship()

    print_board(board)

    # MILESTONE 3: loop — ask for a guess, check it against `ship`,
    # mark "X" or "O" on the board, reprint.
    # MILESTONE 4: stop when every ship cell is hit; print guess count.
    answer = input("Guess (row col): ")
    print(f"You guessed: {answer} — now make it do something!")


if __name__ == "__main__":
    main()
