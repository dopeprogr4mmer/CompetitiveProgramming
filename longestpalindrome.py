import pprint as p
def minimumNumberOfDeletions(string):
	n = len(string)
	rev_string = string[::-1]
	grid = [[0 for x in range(n+1)] for y in range(n+1)]
	max_length = 0
	#print(p.pprint(grid))
	#print(rev_string)
	for i in reversed(range(n)):
		for j in reversed(range(n)):
			if string[i] == rev_string[j]:
				grid[i][j] = grid[i+1][j+1] + 1
			else:
				grid[i][j] = max(grid[i+1][j+1], grid[i+1][j], grid[i][j+1])

			if grid[i][j]>max_length:
				max_length = grid[i][j]
	#p.pprint(grid)

	return max_length


max_length = minimumNumberOfDeletions('rahul')
print(max_length)