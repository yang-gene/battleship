# Battleship-Python

A very simple Battleship game for the console, written in plain Python. Adapted from this tutorial: <https://bigmonty12.github.io/battleship>

Read about the game and its rules here: <https://en.wikipedia.org/wiki/Battleship_(game)>

Run it:

```
python3 battleship.py
```

### Step 1: Build and print the game board

Fill in `build_board` and `print_board` — a 5x5 grid of `O` characters.

Useful references:

- [Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [List comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Loops in Python](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

### Step 2: Place a ship

Fill in `build_ship` — random length, random orientation, random position, fully on the board. Keep it hidden from the player!

Useful references:

- [The random module](https://docs.python.org/3/library/random.html) (`random.randint` is your friend)
- [Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [zip()](https://docs.python.org/3/library/functions.html#zip)

### Step 3: Take guesses and write the game logic

Fill in `user_guess` and `update_board`, then wire up the loop in `main` — keep guessing until every ship cell is hit.

Useful references:

- [input()](https://docs.python.org/3/library/functions.html#input)
- [while loops](https://docs.python.org/3/reference/compound_stmts.html#while)
- [if-else statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

### Step 4: Play the game

Features to implement next:

- Track and print how many guesses it took to win
- Multiple ships of different lengths (classic: 5, 4, 3, 3, 2)
- Colored output for hits and misses ([ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors))
- Make a 2-player hotseat version of the game!
