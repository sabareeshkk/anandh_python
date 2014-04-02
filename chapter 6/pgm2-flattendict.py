# Program to write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

def flatten_dict(a,result=None):
	if result==None:
		result={}
	k={}
	for x,y in a.items():
		if isinstance(y,dict):
			for i,j in y.items():
				k[x+'.'+i]=j
			flatten_dict(k,result)
		else:
			result[x]=y

	return result
print flatten_dict({'a': 1, 'b': {'x': {'d':2}, 'y': 3}, 'c': 4})
	
