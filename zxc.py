import math
def makeItOne(N):
    # code here 
    #print(int(N))
    count = 0
    l = [int(math.pow(2,x)) for x in range(int(math.log2(N)+1))]
    #print(l)

    while(N!=1):
    	if N in l:
    		count+=l.index(N)
    		N = 1
    	else:
    		#l = [x for x in l if x<N]
    		N -= l[-1]
    		count+=1

    return count

count = makeItOne(math.pow(2,63)-7173543545334533543)
print(count)