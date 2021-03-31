def factorial(n):					#recursion
	if n<0:
		return -1
	if n== 1:
		return 1
	else:
		return n*factorial(n-1)
	


def memoFact(N):						#memoisation   using dict
    arr = {}
    if N in arr:
        return arr[N]
    elif N == 0 or N == 1:
    	arr[N] = 1
    	return arr[N]
    else:
    	factorial = N*memoFact(N - 1)
    	arr[N] = factorial
    #print(arr[N])
    return factorial

def dpFact(n):							#no-recurssion DP using array/list
	memo = [None]*(n+1)
	#print(memo[0])
	if n<0:
		return -1
	if n == 0 or n == 1:
		return 1
	memo[0] = memo[1] = 1
	for i in range(2,n+1):
		memo[i] = memo[i-1]*i
	return memo[n]

#arr = {}

if __name__ == '__main__':
	try:
		n = int(input("Enter a number: "))
		#print(n)
		fact = dpFact(n)
		print(f'The factorial of {n} is {fact}')
	except:
		print('Invalid Input. Pass numeric values only!')

#a = int(input("enter: "))
#print(memoFact(a))
'''arr = {3:1}
if 3 in arr:
	print(arr[3])
	'''
