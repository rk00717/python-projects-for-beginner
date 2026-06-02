# python-projects-for-beginner

A collection of Python console games built for beginners to read, learn from, and run. All games share a common abstract base class and launch from a single menu.

Includes a compiled `.exe` for Windows — no Python installation needed to play.

## Games

| # | Game | Highlight |
|---|---|---|
| 1 | Madlib | JSON-driven word bank, fill-in-the-blank story generator |
| 2 | Guess The Number | Classic number guessing with attempt tracking |
| 3 | Rock Paper Scissors | Input vs random computer choice |
| 4 | Hangman | Word dictionary from JSON, visual hang stages |
| 5 | Tic Tac Toe | Two modes — `DumbComputer` (random) and `SmartComputer` (Minimax algorithm) |
| 6 | Minesweeper | Grid-based board, weighted neighbour bomb counting, dig system |

## Architecture

- `GameBase` — abstract base class (`ABC`) with `start_game()` method. Every game inherits and implements it
- `main.py` — builds a playlist dict, loops the menu, instantiates and launches the selected game
- Each game is a self-contained module under `rkode/`
- Word data for Hangman and Madlib loaded from JSON files

## Run

**Option 1 — compiled exe (Windows):**
```
games/dist/main.exe
```

**Option 2 — Python:**
```bash
cd games
python main.py
```

## Stack

Python · ABC · JSON · Console UI
