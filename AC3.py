# IMPLEMENTATION OF AC3 ALGORITHM

import queue
from CSP import *

#THE MAIN AC-3 ALGORITHM
def AC3(csp):
	q = queue.Queue()

	for arc in csp.constraints:
		q.put(arc)

	i = 0
	while not q.empty():
		(Xi, Xj) = q.get()

		i = i + 1 

		if Revise(csp, Xi, Xj):
			if len(csp.values[Xi]) == 0:
				return False

			for Xk in (csp.peers[Xi] - set(Xj)):
				q.put((Xk, Xi))

	#display(csp.values)
	return True 



#WORKING OF THE REVISE ALGORITHM
def Revise(csp, Xi, Xj):
	revised = False
	values = set(csp.values[Xi])

	for x in values:
		if not isconsistent(csp, x, Xi, Xj):
			csp.values[Xi] = csp.values[Xi].replace(x, '')
			revised = True 

	return revised 



#CHECKS IF THE GIVEN ASSIGNMENT IS CONSISTENT
def isconsistent(csp, x, Xi, Xj):
	for y in csp.values[Xj]:
		if Xj in csp.peers[Xi] and y!=x:
			return True

	return False


#DISPLAYS THE SUDOKU IN THE GRID FORMAT
def display(values):
    for r in rows:
    	if r in 'DG':
    		print ("------------------------------------------------------------------------------")
    	for c in cols:
    		if c in '47':
    			print (' | ', values[r+c], ' ',end=' ')
    		else:
    			print (values[r+c], ' ',end=' ')
    	print (end='\n')

        

#CHECKS IF THE SUDOKU IS COMPLETE OR NOT
def isComplete(csp):
	for variable in squares:
		if len(csp.values[variable])>1:
			return False
	return True


#WRITES THE SOLVED SUDOKU IN THE FORM OF A STRING
def write(values):
	output = ""
	for variable in squares:
		output = output + values[variable]
	return output