# INCLUDES THE HELPER FUNCTIONS AND VARIABLES USED BY THE PROGRAM


digits =  cols = "123456789"
rows = "ABCDEFGHI"


#FINDING THE CROSS PRODUCT OF TWO SETS 
def cross(A, B):
	return [a + b for a in A for b in B]

squares = cross(rows, cols)




   	



