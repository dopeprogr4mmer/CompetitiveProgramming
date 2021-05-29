from sys import setrecursionlimit
setrecursionlimit(1000000)
from pprint import pprint
from functools import lru_cache
import time
#pp = pprint.PrettyPrinter() #parameters --> indent, width, depth, stream, compact, sort_dicts

def knapsack_iterative(W,n,val,wt):
	grid = [[0 for i in range(W+1)] for j in range(n+1)]
	#print("hello world")
	#pprint(grid)
	#print(n)
	for i in range(n+1):
		for w in range(W+1):
			if i == 0 or w == 0:
				grid[i][w] = 0
			elif wt[i-1] <= w:
				grid[i][w] = max(val[i-1]+grid[i-1][w-wt[i-1]],grid[i-1][w])
			else:
				grid[i][w] = grid[i-1][w]

	#print(grid)
	return grid[n][W]

@lru_cache(maxsize = None)
#@cache
def knapsack_recursive(W,n,val,wt):
	#val, wt = tuple(val), tuple(wt) 			#error-unhashable type: list
	if n == 0 or W == 0:
		return 0
	if (wt[n-1]>W):
		print(knapsack_recursive.cache_info())
		return knapsack_recursive(W,n-1,val,wt)
	else:
		print(knapsack_recursive.cache_info())
		return max(val[n-1] + knapsack_recursive(W-wt[n-1],n-1,val,wt), knapsack_recursive(W,n-1,val,wt))


val = [x for x in range(20,20000,40)]
wt = [x for x in range(10,10000,10)]
W = 1000


#val = knapsack_recursive(W,len(val),tuple(val),tuple(wt))
#print(val)
print(time.localtime())
print(time.gmtime())
print(time.time())
time.sleep(2)
print(time.time())