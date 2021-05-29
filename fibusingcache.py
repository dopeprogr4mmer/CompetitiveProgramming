from functools import lru_cache

@lru_cache(maxsize = 3, typed = False)  #instant results
def fib_using_cache(n):
	if n <= 1:
		return n
	else:
		return fib_using_cache(n-1) + fib_using_cache(n-2)


def main():
	for i in range(1,401):
		fib = fib_using_cache(i)
		print(f'fib of {i} is {fib}')
		print(fib_using_cache.cache_info())



main()		#@singledispatch