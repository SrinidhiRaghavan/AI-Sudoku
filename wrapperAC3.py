# THE WRAPPER FUNCTION WHICH SOLVES ALL THE SUDOKU PROBLEMS IN THE INPUT FILE USING AC3 AND WRITES THE OUTPUT TO THE OUTPUT FILE 


import sys #For getting the values from command line 
import time 
from CSP import csp
from AC3 import *

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
    
    for grid in array:
        prev = time.time()
        sudoku = csp(grid=grid)
        solved  = AC3(sudoku) 
        boardno = boardno + 1 
        if isComplete(sudoku) and solved: 
            print (boardno)
            print ("Before solving: ", grid)
            print ("After solving: ", write(sudoku.values))
            print ("Running time: ", time.time()-prev, "\n")
            i = i + 1
    

    print ("Number of problems solved is: ", i)
    print ("The complete run time is: ", time.time()-start)