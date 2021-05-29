import pprint as p
def spiral_traversal(matrix, r, c):
	p.pprint(matrix)
	length = r*c
	i, j = 0, 0
	result = []
	result.append(matrix[0][0])
	matrix[0][0] = True
	while(len(result)!=length):
		while(j<c-1 and matrix[i][j+1]!=True):
			j+=1
			result.append(matrix[i][j])
			matrix[i][j]=True
			print('hi',i,j)
		while(i<r-1 and matrix[i+1][j]!=True):
			i+=1
			result.append(matrix[i][j])
			matrix[i][j]=True
			print('hello',i,j)
		while(j>0 and matrix[i][j-1]!=True):
			j-=1
			result.append(matrix[i][j])
			matrix[i][j]=True
			print("tata",i,j)
		while(i>0 and matrix[i-1][j]!=True):
			i-=1
			result.append(matrix[i][j])
			matrix[i][j]=True
			print("goodbye",i,j)
	return result

""""
def spirallyTraverse(self,matrix, r, c): 
        # code here 
        #p.pprint(matrix)
        top = left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        op = []
    
        while True:
            if left > right:
                break
            
            for i in range(left,right+1):
                op.append(matrix[top][i])
            
            top += 1
            
            if top > bottom:
                break
                
            for i in range(top,bottom+1):
                op.append(matrix[i][right])

            right -= 1
            
            if left > right:
                break
        
            #print(m,n,i)
            for i in range(right,left-1,-1):
                op.append(matrix[bottom][i])
                
            bottom -= 1
            
            if top > bottom:
                break
            
            for i in range(bottom,top-1,-1):
                op.append(matrix[i][left])
            
            left += 1
            

        return op
        """

r = 5
c = 5
matrix = [[71, 72, 73, 74, 75],
          [56, 66, 67, 68, 69],
          [91, 10, 11, 12, 61],
          [13, 14, 15, 16, 25],
          [81, 82, 83, 84, 85]]

result = spiral_traversal(matrix, r, c)
print(result)

