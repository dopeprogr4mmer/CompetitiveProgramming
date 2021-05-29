def replace(string, pattern):
    while(True):
    	if pattern in string:
    		string.replace(pattern,'X')
    		print(string)
    	else:
    		break
        
    print(string)
        
pattern = 'ab'
string = 'abababcab'

#replace('abababcab','ab')
string.replace(pattern,'X')
print(string)

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)