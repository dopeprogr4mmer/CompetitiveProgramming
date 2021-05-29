'''Program for longest common subsequence.
Useful for DNA matching and other utilities like these'''

import pprint as p
def lcs(u,v):				
	lcs_grid = [[0 for i in range(len(v)+1)] for j in range(len(u)+1)]
	p.pprint(lcs_grid)

	max_lcs = 0
	#longest_subword = []
	word = ''

	for r in range(len(u)-1,-1,-1):
		for c in range(len(v)-1,-1,-1):
			print(r,c," ",u,v)
			#max_val = max(lcs_grid[r+1][c+1], lcs_grid[r+1][c], lcs_grid[r][c+1])
			#print(max_val,'dh')
			if u[r] == v[c]:
				lcs_grid[r][c] = 1 + lcs_grid[r+1][c+1]
				word+=v[c]
			else:
				lcs_grid[r][c] = max(lcs_grid[r+1][c+1], lcs_grid[r+1][c], lcs_grid[r][c+1])
				#longest_subword.append(word)
				#word = ''

			if lcs_grid[r][c] > max_lcs:
				max_lcs = lcs_grid[r][c]

	
	p.pprint(lcs_grid)
	print(max_lcs, word)
	return max_lcs

lcs('0elementl','1emelentonm')
