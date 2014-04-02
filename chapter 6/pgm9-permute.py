import itertools

def permute(l):
	p=[]
	for i in itertools.permutations(l,len(l)):
		a=[]
		for j in i:
			a.append(j)
		p.append(a)
	return p
print permute([1,2,3])
