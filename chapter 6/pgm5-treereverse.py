# Program to reverse a nested list recurively


def treereverse(l,):
	l.reverse()
        for i in l:
        	if isinstance(i,list):
	        	treereverse(i)			
	
	return l

print treereverse([[1, 2], [3, [4, 5]], 6])
		

