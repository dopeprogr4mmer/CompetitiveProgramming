#code
def geekonaci(sequence):
    n = sequence[-1]
    sequence = sequence[:-1]
    if len(sequence)==n:
        #print(sequence[n])
        return sequence[n-1]

    print(sequence)
    
    sequence.append(sequence[-1]+sequence[-2]+sequence[-3])
    sequence.append(n)
    return geekonaci(sequence)
        

if __name__ == '__main__':
    arg = input().split(" ")
    arg = [int(x) for x in arg]
    print(geekonaci(arg))
    