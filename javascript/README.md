# Battleship-JavaScript

A simple Battleship game in plain JavaScript. The HTML and CSS shell is provided; `battleship.js` has the constants and stubbed-out functions to guide you — the game logic and UI decisions are yours.

Read about the game and its rules here: <https://en.wikipedia.org/wiki/Battleship_(game)>

Run it over http — `python3 -m http.server` in this folder, then open <http://localhost:8000> (the module script won't load from `file://`).

### Step 1: Render the board and make every click a miss

Get a 10x10 grid on the page, and register clicks so each guess shows up as a miss. Reject repeat guesses.

Useful references:

- [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout)
- [Document.createElement()](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
- [Handling events](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Events)
- [Event delegation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Event_bubbling#event_delegation)

### Step 2: Hide the fleet and score hits

Place every ship in `FLEET` at a random legal spot — no overlaps, nothing out of bounds. Ships stay hidden; a guess on a ship cell is a hit.

Useful references:

- [Arrays in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Math.random()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random)

### Step 3: Win, lose, and play again

The game is won when all 17 ship cells are hit, and lost when the player runs out of guesses — pick a guess cap. Offer a way to play again.

### Step 4: Reveal sunk ships

When a ship's last cell is hit, reveal that whole ship and name it. On a loss, reveal whatever's left of the fleet.

### Ideas for after

- Sound effects, better graphics
- A vs-CPU mode where the computer guesses back
- A 2-player version
