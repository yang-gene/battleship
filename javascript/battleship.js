const BOARD_SIZE = 10;

// Fleet per the official Hasbro rules — 17 hits total to sink everything.
const FLEET = [
	{ name: "carrier", length: 5 },
	{ name: "battleship", length: 4 },
	{ name: "destroyer", length: 3 },
	{ name: "submarine", length: 3 },
	{ name: "patrol boat", length: 2 },
];

/**
 * Owns the game: builds the starting state, places the fleet, and wires up
 * whatever needs to react to the player's guesses. How you represent state
 * (a closure over locals, one object, classes...) is up to you.
 *
 * @returns {object} whatever your game needs to expose — maybe nothing!
 */
function createGame() {
	// TODO
}

/**
 * Builds an empty board. What a "board" is — 2d array, flat array, Map keyed
 * by coordinate — is one of the fun decisions. Each cell needs to be able to
 * say: is there a ship here, and has this spot been guessed?
 *
 * @returns {object} board representation of your choosing
 */
function createBoard() {
	// TODO
}

/**
 * Puts every ship in FLEET onto the board at random spots — horizontal or
 * vertical, in bounds, no overlaps.
 *
 * @param {object} board your board representation
 */
function placeShips(board) {
	// TODO
}

/**
 * Finds a random legal position for one ship of the given length. Expect
 * collisions with already-placed ships — decide how to retry.
 *
 * @param {object} board your board representation
 * @param {number} length how many cells the ship covers
 */
function randomPlacement(board, length) {
	// TODO
}

/**
 * Draws the current state into #gameboard (and #guessCount / #gameInfo if you
 * use them). style.css has classes you can lean on, or go your own way —
 * re-render everything each time, or update just the cell that changed.
 *
 * @param {object} state whatever render needs to know
 */
function render(state) {
	// TODO
}

// TODO: start a game, and listen for clicks on the board so a click becomes a
// guess — one listener on #gameboard, or one per cell; dealer's choice.
