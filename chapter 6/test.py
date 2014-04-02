import time
def fib(n):
	if n is 0 or n is 1:
        	return 1
    	else:
        	return fib(n-1) + fib(n-2)

def profile(f):
	cache={}
	def g(x):
		t=0
		if x not in cache:
			start=time.time()
        		cache[x]=f(x)
        		t=time.time()-start
		return str(t)+'  sec'
    	return g

fib = profile(fib)
print fib(100)
