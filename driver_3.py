# MAIN DRIVER PROBLEM TO SOLVE AN INPUT SUDOKU PUZZLE


import sys 					#For getting the values from command line 
import time 
from CSP import csp
from Backtrack import *
#from AC3 import *			#Uncomment this if you want to test AC3

#THE MAIN FUNCTION GOES HERE
if __name__ == "__main__":
    '''
    The function takes arguments from commandline
    Argument 1 - Python file name 
    Argument 2 - Input String Showing the Sudoku 
    '''
    if len(sys.argv)==2:
        grid = sys.argv[1]
        assert len(grid) == 81
        start = time.time()
        sudoku = csp(grid=grid)
        solved = Backtracking_Search(sudoku)
        #solved = AC3(sudoku) 

        f = open("output.txt", "w")

        if solved!="FAILURE":
            display(solved) 		#Displays the solved puzzle in the sudoku format
            print (write(solved))
            f.write(write(solved)+"\n")
            print ("This puzzle was solved in: ", time.time()-start," seconds")
            print ("Perfectly solved")
        else:
        	print ("Not solved")

        f.close()
        '''	
        if isComplete(sudoku) and solved:
        	display(solved) 		#Displays the solved puzzle in the sudoku format
        	print ("This puzzle was solved in: ", time.time()-start," seconds")
        	print ("Perfectly solved")
        else:
        	print ("Not solved")

        '''
    else:
        print ("INVALID NUMBER OF INPUTS") 
