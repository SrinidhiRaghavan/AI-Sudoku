# THE WRAPPER FUNCTION WHICH SOLVES ALL THE SUDOKU PROBLEMS IN THE INPUT FILE USING BACKTRACKING AND WRITES THE OUTPUT TO THE OUTPUT FILE 

import sys #For getting the values from command line 
from CSP import csp
from Backtrack import *
import time 

#THE MAIN FUNCTION GOES HERE
if __name__ == "__main__":
    '''
    The function takes arguments from commandline
    Argument 1 - Python file name 
    Argument 2 - Input String Showing the Sudoku 
    '''
    array = []  
    with open("sudokus_start.txt", "r") as ins:
        for line in ins:
            array.append(line)

    ins.close()
    i = 0
    boardno = 0
    start = time.time()
    f = open("output.txt", "w")

    for grid in array:
        startpuzle = time.time()
        boardno =  boardno + 1
        sudoku = csp(grid=grid)
        solved  = Backtracking_Search(sudoku) 
        print ("The board-", boardno, " takes ", time.time() - startpuzle, " seconds")
        if solved!="FAILURE": 
            f.write(write(solved)+"\n")
            i = i + 1
    f.close()

    print ("Number of problems solved is: ", i)
    print ("Time taken to solve the puzzles is: ", time.time()-start)