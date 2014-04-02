
# Program to map a function over nested list

def treemap(f,l):
	for i in range(len(l)):
		if isinstance(l[i],list):
			treemap(f,l[i])
		else:
			k=f(l[i])
			l.remove(l[i])
			l.insert(i,k)
	return l

print treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
	
