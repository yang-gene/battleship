# Battleship

Code Club RDU beginner project — build console Battleship, in JavaScript or Python. Pick your language, open the folder, go.

## Run it (works right away)

```
cd javascript && node battleship.js
# or
cd python && python3 battleship.py
```

You'll see an empty 5x5 board and a guess prompt. Your job: make the game real.

## Milestones

Work in order. Stopping after any milestone still feels finished.

1. **Print the board** — already done in the starter. Read the code, understand it, change the board size if you want.
2. **Place a ship** — fill in `placeShip` / `place_ship`: one 3-cell ship, random spot, horizontal or vertical, hidden from the player.
3. **Guess loop** — read `row col` guesses, mark hits `X` and misses `O`, reprint the board after each guess.
4. **Win the game** — detect when the whole ship is sunk; print a win message with the guess count.

## Stretch

- Multiple ships of different lengths (classic: 5, 4, 3, 3, 2)
- Two-player hotseat — take turns firing at each other's boards
- Limited ammo mode, or a computer opponent that guesses back

## Team tips

- Rotate the keyboard every ~10 minutes (driver/navigator)
- Talk before you type — agree on the plan for the current milestone
- Stuck on setup? Flag a lead — that's what they're floating for
