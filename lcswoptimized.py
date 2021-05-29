import pprint as p
def lcw(u,v):
	#print(len(u),len(v))
	LCW = [[0 for i in range(len(v)+1)] for j in range(len(u)+1)]
	
	maxLCW = 0
	longest_subword = []

	for c in range(len(v)-1, -1, -1):
		for r in range(len(u)-1, -1, -1):
			#print(u,v)
			#print(r)
			if u[r] == v[c]:
				#print(LCW[r+1][c+1])
				LCW[r][c] = 1 + LCW[r+1][c+1]
				#p.pprint(LCW)
				#print()
			else:
				LCW[r][c] = 0
			if LCW[r][c] > maxLCW:
				maxLCW = LCW[r][c]
	p.pprint(LCW)
	for i in range(len(LCW)):
		word = ''
		temp = maxLCW
		if maxLCW in LCW[i]:
			#print('jv')
			x = i
			#y = LCW[i].index(maxLCW)s
			while temp>0:
				#print(temp,x,u[x])
				word += u[x]
				x+=1
				#y+=1
				temp-=1
			#else:
			#print(word)
			longest_subword.append(word)
	#print(longest_subword)


	return (maxLCW,longest_subword)

try:
	if __name__ == '__main__':
		length, word_list = lcw('safarfjkin','adhksjsafakjkin')
		print(f'Length of longest common subword is {length}')
		print(f'the words are:')
		for word in word_list:
			print(word)
except Exception:
	errno = 50159747054
	print(f'Hey Phantom! there is a {errno:#x} error')
