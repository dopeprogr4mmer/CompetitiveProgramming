counter=0
def rpower(a, n):
    'returns a to the nth power'
    global counter          # counts number of multiplications

    if n == 0:
        return 1
    # if n > 0:
    tmp = rpower(a, n//2)

    if n%2 == 0:
        counter += 1
        return tmp*tmp      # 1 multiplication

    else:
        counter += 2
        return a*tmp*tmp    # 2 multiplications
print(rpower(2, 10000))