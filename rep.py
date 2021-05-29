def solve(s, n, r):
	coke = s
	while r>0:
		exp = ''
		for i in coke:
			if i == '1':
				exp += '10'
			else:
				exp += '01'

		coke = exp
		print(coke)
		r-=1
	return coke[n+1]

s = solve('101', 2, 3)
print(s)