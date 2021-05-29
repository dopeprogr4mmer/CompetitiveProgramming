def decimal_to_binary(n):
	binary = ""
	while n>=2:
		bit = n%2
		n = n//2
		binary = str(bit) + binary
		#print(binary,';',n)
	binary = str(n) + binary
	print(binary)

decimal_to_binary(1)