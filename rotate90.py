import pprint as p
def rotate(matrix, n):
	p.pprint(matrix)
	print()
	transpose(matrix, n)
	#reverse_row(matrix, n)
	reverse_col(matrix, n)
	print_matrix(matrix)

def transpose(matrix, n):
	for i in range(n):
		for j in range(i, n):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	p.pprint(matrix)
	print()

def reverse_row(matrix, n):
	x = 0
	y = n-1
	for i in range(n):
		while(y>x):
			matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]
			x+=1
			y-=1

def reverse_col(matrix, n):
	for i in range(n):
		x = 0
		y = n-1
		#print(i)
		while(y>x):
			matrix[x][i], matrix[y][i] = matrix[y][i], matrix[x][i]
			x+=1
			y-=1


def print_matrix(matrix):
	p.pprint(matrix)




matrix = [[41, 42, 43, 44, 45, 46],
		  [47, 48, 49, 10, 11, 12],
          [13, 14, 15, 16, 17, 18],
          [19, 20, 21, 22, 23, 24],
          [25, 26, 27, 28, 29, 30],
          [31, 32, 33, 34, 35, 36]]

rotate(matrix, len(matrix))