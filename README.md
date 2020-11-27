# Sudoku Solver

Sudoku Solver using recursion and backtracking.

## Usage walk-through

1. Prepare a sudoku puzzle as a 9x9 2D array. Two examples can be 
found in `test_boards.txt`.
2. Use `solve(board)`, where the argument "board" is the 2D array of 
the sudoku puzzle, if executing the `baseSudoku.py` version.
3. Use `main(board)` when executing the `visualSudoku.py` version.
4. Change the frames per second, box size, boarder size and grid line
size with the variables at the top of the `visualSudoku.py` file.

## Requirements

- Python 3
- Pygame (for `visualSudoku.py`)

## Bugs

- When asking for more solutions in `visualSudoku.py` it gives the 
same solution repeatedly.
