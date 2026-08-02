// Battleship — JavaScript starter
// Run: node battleship.js  (Node 18+)

const readline = require("node:readline/promises");

const SIZE = 5;
const SHIP_LENGTH = 3;

// board[row][col]: "." = unknown, "X" = hit, "O" = miss
function makeBoard() {
  return Array.from({ length: SIZE }, () => Array(SIZE).fill("."));
}

function printBoard(board) {
  console.log("  " + [...Array(SIZE).keys()].join(" "));
  board.forEach((row, r) => console.log(r + " " + row.join(" ")));
}

// MILESTONE 2: return the ship's cells as a list of [row, col] pairs —
// SHIP_LENGTH cells in a line (horizontal or vertical), random position,
// fully inside the board.
function placeShip() {
  // TODO
  return [];
}

async function main() {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  const board = makeBoard();
  const ship = placeShip();

  printBoard(board);

  // MILESTONE 3: loop — ask for a guess, check it against `ship`,
  // mark "X" or "O" on the board, reprint.
  // MILESTONE 4: stop when every ship cell is hit; print guess count.
  const answer = await rl.question("Guess (row col): ");
  console.log(`You guessed: ${answer} — now make it do something!`);

  rl.close();
}

main();
