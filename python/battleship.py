# Battleship — build the classic game in the console.
#
# THE MAP: read the Thought Process in README.md first. Then work the
# steps below in order, running as you go:  python3 battleship.py
# Checkpoints at the bottom show you when each layer works — expected
# output is in the README.

import copy
import random
from enum import Enum
from typing import List


# ── The vocabulary of the game — given, so we all speak the same language ──
# (Enums are just named constants grouped together. Read, don't memorize.)

class Orientation(Enum):
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"


class ShipType(Enum):
    DESTROYER = "destroyer"
    SUBMARINE = "submarine"
    CRUISER = "cruiser"
    BATTLESHIP = "battleship"
    CARRIER = "carrier"


class CellState(Enum):
    HIT = "hit"
    MISS = "miss"
    SHIP = "ship"
    EMPTY = "empty"


Point2D = tuple  # a (row, col) pair
BoardData = List[List[CellState]]

# Display constants — change the markers if you have better taste than us
DIM = 10
EMPTY_MARKER = "◯"
MISS_MARKER = "⤫"
HIT_MARKER = "⏺"
SHIP_MARKER = "☸"


class Ship:
    # STEP 1: a ship needs to know...
    #   - its length
    #   - its position: a (row, col) for its top-left cell
    #   - its orientation: Orientation.HORIZONTAL or VERTICAL
    #   - whether it has been placed on a board yet
    #   - how close it is to sinking (hint: hit points that start at length
    #     and count down; at 0 the ship is sunk)
    def __init__(self, length: int) -> None:
        self.length = length
        self.orientation = Orientation.VERTICAL
        self.position = (0,0)
        self.placed = False
        self.health = self.length

# STEP 2: the classic fleet — build a dict with one Ship per ShipType:
# destroyer 2, submarine 3, cruiser 3, battleship 4, carrier 5
ALL_SHIPS = {
    ShipType.DESTROYER: 2,
    ShipType.SUBMARINE: 3,
    ShipType.CRUISER: 3,
    ShipType.BATTLESHIP: 4,
    ShipType.CARRIER: 5
}


class Board:
    # A board owns two things (see Thought Process #2 — data vs display):
    #   self.ships — its own fleet: a fresh copy of ALL_SHIPS
    #                (careful: a shared copy is a classic bug — look up deepcopy)
    #   self.hits  — a DIM x DIM grid of CellState tracking every shot so far,
    #                all EMPTY to start

    def __init__(self) -> None:
        self.ships = [] # List of Ships
        self.guesses = [] # List of tuples (points) (X, Y, CellState)
        self.grid = []

    # STEP 4: combine self.guesses and ship positions into one grid for display.
    # Start from a copy of self.guesses, then stamp CellState.SHIP over the cells
    # each placed ship covers. If add_ships is False, skip the stamping —
    # that's what your opponent sees.
    def _build_board_state(self, add_ships: bool) -> BoardData:
        # List[List[CellState]]
        boardState = [ [CellState.EMPTY]*10 for i in range(10) ]
        for guess in self.guesses:
            boardState[guess[0], guess[1]] = guess[2]

        if add_ships:
            for ship in self.ships:
                headX = ship.position[0]
                headY = ship.position[1]
                for i in range(ship.length):
                    if ship.orientation == Orientation.HORIZONTAL:
                        if boardState[headX + i][headY] == CellState.EMPTY:
                            boardState[headX + i][headY] = CellState.SHIP
                    else:
                        if boardState[headX][headY + 1] == CellState.EMPTY:
                            boardState[headX][headY + 1] = CellState.SHIP

        return boardState


    # STEP 5: print the grid — column numbers 0-9 across the top, row letters
    # A-J down the side (chr(ord('A') + i) is your friend), one marker per cell.
    # Expected look: checkpoint 1 in the README.
    def show(self, show_ships=False):

        rowLabels = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J"
        }
        for i in range(11):
            if i == 0:
                print(" 0123456789")
            else:
                print(rowLabels[i] + "0000000000")


    # STEP 6: the rules of placement (Thought Process #5 — this is the tricky one):
    #   - the whole ship must fit on the board (check the far end!)
    #   - it can't overlap a ship that's already placed
    # If the spot is bad, return False and change nothing.
    # If it's good: save position + orientation on the ship, mark it placed,
    # return True.
    def place_ship(self, type: ShipType, position: Point2D, orientation: Orientation) -> bool:
        # Check if space required for ship is empty
        ship_length = ALL_SHIPS[type]

        if orientation == Orientation.VERTICAL:
            for i in range(ship_length):
                if self.grid[position[0]][position[1] + i] != CellState.EMPTY:
                    return
        else:
            for i in range(ship_length):
                if self.grid[position[0] + i][position[1]] != CellState.EMPTY:
                    return

        # Create the ship 
        new_boat = Ship(ship_length)
        new_boat.orientation = orientation
        new_boat.position = position
        new_boat.placed = True

        # Add to board array of ships
        self.ships.append(new_boat)

    # STEP 7: ready = every ship in the fleet has been placed
    def is_ready(self) -> bool:
        pass  # TODO

    # STEP 8: did a shot at this position hit a ship?
    # For now just return True (hit) or False (miss).
    # Milestone 1 in the README will grow this: record the shot in self.hits,
    # damage the ship, detect sinking.
    def make_guess(self, position: Point2D) -> bool:
        pass  # TODO


# ── THE GAME — once the checkpoints pass, make the pieces play ──
# (README milestones, in order:)
#
#   1. Upgrade make_guess: record HIT/MISS in self.hits, damage the ship
#      (hp), mark it sunk at 0. Add is_defeated() — True when the whole
#      fleet is sunk.
#   2. parse_position("B4") -> (1, 4). Reject junk input and repeat guesses.
#   3. random_place_all(board) — random spot + orientation per ship, retry
#      until place_ship says True.
#   4. play() — the loop: show boards, your shot (input()), CPU's random
#      shot, first fleet fully sunk loses.
#
# def play():
#     ...


if __name__ == "__main__":
    # ✅ CHECKPOINT 1 — two empty boards (steps 1-5).
    # Expected output: README. Don't move on until yours matches.
    my_board = Board()
    my_board.place_ship(ShipType.BATTLESHIP, (0,0), Orientation.VERTICAL)
    cpu_board = Board()
    cpu_board.show()
    print("\n---------------------\n")
    my_board.show(show_ships=True)

    # ✅ CHECKPOINT 2 — place the fleet (steps 6-7). Ready flips to True
    # only when all five ships are down. Try an off-board or overlapping
    # placement too — it should return False and change nothing.
    # my_board.place_ship(ShipType.CARRIER, (0, 0), Orientation.VERTICAL)
    # my_board.place_ship(ShipType.SUBMARINE, (0, 1), Orientation.VERTICAL)
    # print("Ready:", my_board.is_ready())   # False — three ships to go
    # my_board.place_ship(ShipType.BATTLESHIP, (0, 2), Orientation.VERTICAL)
    # my_board.place_ship(ShipType.DESTROYER, (0, 3), Orientation.VERTICAL)
    # my_board.place_ship(ShipType.CRUISER, (0, 4), Orientation.VERTICAL)
    # my_board.show(show_ships=True)
    # print("Ready:", my_board.is_ready())   # True

    # ✅ CHECKPOINT 3 — take a shot (step 8).
    # (2, 1) is part of the submarine you just placed — hit.
    # (3, 1) is open water — miss.
    # print("Hit:", my_board.make_guess((2, 1)))   # True
    # print("Hit:", my_board.make_guess((3, 1)))   # False

    # Then: milestones. Uncomment when play() exists.
    # play()
