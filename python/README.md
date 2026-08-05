# Battleship-Python

Build the classic Battleship game in the console. Starter design by Zane.

Read about the game and its rules here: <https://en.wikipedia.org/wiki/Battleship_(game)>

Run it (from this folder, in the Codespace terminal or your own):

```
python3 battleship.py
```

## The Thought Process (read this first — it's the map)

1. What is the board going to look like?
    - `my_board` and `cpu_board`, each a 2D matrix (10x10)
    - Characters for hit, miss, ship, and empty
    - Proof of concept: print a basic board, add labels (A0 thru J9)
2. What state do I need to track, and how is it separate from what's displayed?
    - Player and CPU need separate boards and separate past guesses
    - Decouple the board's *data* from the board's *visual* — a `Board` class stores ship placement and hit data; a display function renders it
    - Ships should only be visible to the board owner
3. How will I represent ships? Position, orientation, and length
4. Placement validity (within bounds + not overlapping) comes up everywhere — it's tricky and has more than one solution
5. Displaying hits & ships means merging data from two sources
    - Watch out: shallow copy doesn't clone the nested lists in the matrix (deep vs shallow copy!)
    - True/False per cell isn't enough — you need Hit/Miss/Ship/Empty
6. Then the game loop: are players ready, whose turn, win condition, user input

## Checkpoints

`battleship.py` walks you through steps 1-8 as comments; checkpoint code at the bottom of the file tells you when each layer works. Checkpoint 1 (empty boards) should look like:

```
  0 1 2 3 4 5 6 7 8 9
A ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
B ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
C ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
D ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
E ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
F ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
G ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
H ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
I ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
J ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯ ◯
```

Checkpoint 2 places five ships down the left side and `Ready:` flips to `True`; checkpoint 3 fires two shots — `(2, 1)` hits the submarine, `(3, 1)` misses.

## Milestones — make it a game

1. **Record guesses** — grow `make_guess`: save HIT/MISS into `self.hits`, damage the ship (`hp`), mark it sunk at 0, add `is_defeated()`.
2. **Read the player's shot** — `parse_position("B4")` → `(1, 4)`. Reject junk and repeat guesses.
3. **Place ships randomly** — random position + orientation per ship, retry until `place_ship` accepts.
4. **The game loop** — alternate turns (CPU guesses randomly), show both boards, first fleet fully sunk loses.
5. **Stretch** — smarter CPU (hunt nearby after a hit), let the player place ships by hand, guess counter, sound effects via `print('\a')`...

## Useful references

- [Classes](https://docs.python.org/3/tutorial/classes.html) — `Ship` and `Board`
- [Enums](https://docs.python.org/3/library/enum.html) — the given vocabulary
- [copy.deepcopy](https://docs.python.org/3/library/copy.html) — the shallow-copy trap in Thought Process #5
- [List comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) — building the 10x10 grid
- [input()](https://docs.python.org/3/library/functions.html#input) and [while loops](https://docs.python.org/3/reference/compound_stmts.html#while) — the game loop
- [The random module](https://docs.python.org/3/library/random.html) — CPU placement and shots
