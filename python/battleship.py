# Battleship — see README.md for step-by-step instructions and references

import random

# board dimensions (the board is dims x dims)
dims = 5


# build the game board: a 2d list filled with 'O' characters, dims rows by dims cols
# (hint: list comprehension)
def build_board(dims):
    pass


# print the board, one row per line
def print_board(board):
    pass


# place a ship on the board:
#   - random length (2 up to dims)
#   - random orientation (horizontal or vertical)
#   - random position, fully inside the board
# return the ship as a list of (row, col) tuples
def build_ship(dims):
    pass


# ask the player for a row and a column, return them as a (row, col) tuple
# (remember: players count from 1, lists count from 0)
def user_guess():
    pass


# handle one guess:
#   - already guessed? tell them
#   - hit? mark 'X' on the board and remove that cell from the ship
#   - miss? let them know
# return the updated board
def update_board(guess, board, ship, guesses):
    pass


def welcome_message():
    print('Welcome to Battleship!')
    print('A battleship is hidden in the board. Guess rows and columns to sink it!')


# the game loop: build the board and the ship,
# keep taking guesses until every ship cell is hit
def main():
    welcome_message()
    # TODO: build_board, build_ship, then loop while the ship still has cells:
    #       take a guess, update the board, print the board
    print('Now build the game!')


main()
