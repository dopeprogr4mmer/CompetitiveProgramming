from itertools import combinations, permutations
def AB(a, k):
	#print(a)
	t = len(a)
	l = []
	#print(a)
	X = list(permutations(a, t))
	for i in X:
		y = "".join(i)
		if y.count('a') == 2 and y.count('b') == 2 and y not in l:
			l.append(y)
	return l[k]



a = input()
b = a.split()
x, y, z = int(b[0]), int(b[1]), int(b[2])
m , n = '', ''
for i in range(x):
	m+='a'
for j in range(y):
	n+='b'
o = m + n
j = AB(o, z-1)
print(j)
