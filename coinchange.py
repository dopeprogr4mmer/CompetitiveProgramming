from functools import lru_cache
from pprint import pprint

@lru_cache(maxsize = None)
def coin_change_recursive(arr, m, n):
	# Recursive Python3 program for coin change problem.
	# Returns the count of ways we can sum# S[0...m-1] coins to get sum n

	if n == 0:
		return 1
		# If n is 0 then there is 1 solution (do not include any coin)

	if n < 0:
		return 0
		# If n is less than 0 then no solution exists

	if m<=0 and n>0:
		return 0
		# If there are no coins and n is greater than 0, then no solution exist

	return coin_change_recursive(arr, m-1, n) + coin_change_recursive(arr, m, n-arr[m-1])
	# count is sum of solutions (i)including S[m-1] (ii) excluding S[m-1]

def coin_change_iterative(arr, m, n):
	grid = [[0 for i in range(n+1)] for j in range(m+1)]
	#pprint(grid)
	grid[0][0] = 1

	for x in range(1,m+1):
		#print(arr[x-1],'sfgkskljdfg')
		for y in range(n+1):
			if y == 0:
				#if n=0 only 1 solution i.e. no coins
				grid[x][y] = 1
			elif arr[x-1]<=n:
				#sum of solutions (i)including S[m-1] (ii) excluding S[m-1]
				grid[x][y] = grid[x-1][y]+grid[x][y-arr[x-1]]
			else:
				grid[x][y] = grid[x-1][y]	
			#print(grid[x][y])

	pprint(grid)
	return grid[m][n]

def coin_change_iterative_optimised(arr, m, n):
	# table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(n+1)]
 
    # Base case (If given value is 0)
    table[0] = 1
 
    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0,m):
        for j in range(arr[i],n+1):
            table[j] += table[j-arr[i]]
            #p#rint(i, j, table[j])
 
    return table[n]

arr = [1, 2, 3, 5]
n = 5

v = coin_change_iterative_optimised(tuple(arr), len(arr), n)
print(v)