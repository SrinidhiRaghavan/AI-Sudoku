# Solving Sudoku using Backtracking and AC-3 Algorithm #

## Introduction ##

In a standard Sudoku puzzle (9x9 grid), there are 81 variables/tiles in total. Each variable is named by its row and its column, and must be assigned a value from 1 to 9, subject to the constraint that no two cells in the same row, column, or box may contain the same value. The initial configuration of sudoku is a partially filled board. The objective is to solve the puzzle such that all the constraints are satisfied. As the given problem has a list of constraints to be satisfied, CSP solutions work efficiently for the sudoky problem as well


## Representation of the Grid ##

The Sudoku Grid is represented as a dictionary in python.  The keys of the dictionary will be the variable names, each of which corresponds directly to a location on the board. In other words, we use the variable names Al through A9 for the top row (left to right), down to I1 through I9 for the bottom row. For example, in the example board above, we would have sudoku["B1"] = 9, and sudoku["E9"] = 8. The number 0 is used to represent the tiles which are not filled. 


## Code Description ##

wrapper : Runs Backtracking on all the sudoku problems in the file sudoku_start.txt

wrapperAC3 : Runs AC3 on all the sudoku problems in the file sudoku_start.txt

driver_3 : Accepts a commandline sudoky grid in the form of string as an input and writes the solved puzzle to the file output.txt

CSP : Defines the CSP class 

AC3 : Implementation of AC3

Backtrack : Implementation of Backtracking + MRV + FC

helper : Consists of a couple of helper functions used across the problems



## Environment ##

Language : Python-3


## How to execute ? ##

Run python driver_3.py <input_string>

Each Sudoku puzzle is represented as a single line of text, which starts from the top-left corner of the board, and enumerates
the digits in each tile, row by row. 

In order to solve all the puzzles and write their output to a text file, the wrapperAC3 file has to be executed. This file is executed as follows:

python wrapperAC3.py 


## Result ## 
