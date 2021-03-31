import re                #Regular expression

for i in range(32,10_000):
	ch = chr(i)             #Character with the unicode i
	if re.match('\d', ch):  #If it is a digit
	    print(ch, end = ' ')

print(" ")


