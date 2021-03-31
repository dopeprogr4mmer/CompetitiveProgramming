import sys
sys.setrecursionlimit(10**6)

def findOperands(string_list,operator):
	#string_list = list(string)
	index = string_list.index(operator)
	##print(string_list)
	#index = string_list.index(operator)
	operand1 = []
	operand2 = []
	temp_result = 0
	##print(index)
	for i in range(index-1,-1,-1):
		if string_list[i].isnumeric() or string_list[i]=='.':
			operand1.insert(0,string_list[i])
		else:
			break
	for j in range(index+1,len(string_list)):
		if string_list[j].isnumeric() or string_list[j]=='.':
			operand2.append(string_list[j])
		else:
			break

	#print(operand1,operand2)
	temp_operand1 = ''.join(str(elem1) for elem1 in operand1)
	temp_operand2 = ''.join(str(elem2) for elem2 in operand2)

	return temp_operand1, temp_operand2, index



def evaluateString(string):
	if len(string) == 1:
		#print(string)
		return float(string)

	##print(string[0],string[-1])
	operator_list = ['*','/','+','-']


	if not(string[0].isnumeric() and string[-1].isnumeric()):
		return -1	

	string_list = list(string)

	for var in string:
		if not (var in operator_list or var.isnumeric() or var=='.'):
			return -1 
	

	for operator in operator_list:
		if operator in string:
			if '*' in string_list:
				#print(string_list)
				#global index
				operand1, operand2, index = findOperands(string_list,'*')
				temp_result = round(float(operand1)*float(operand2),2)
				##print(temp_result)


			elif '/' in string_list:
				##print(string_list)
				#global index
				operand1, operand2, index = findOperands(string_list,'/')
				temp_result = round(float(operand1)/float(operand2),2)
				##print(temp_result)

			elif '+' in string_list:
				#global index
				operand1, operand2, index = findOperands(string_list,'+')
				temp_result = float(operand1)+float(operand2)
				##print(temp_result)

			elif '-' in string_list:
				#global index
				operand1, operand2, index = findOperands(string_list,'-')
				temp_result = float(operand1)-float(operand2)
				##print(temp_result)

			##print(string_list)	

			
			##print(string_list,index)
			x = index+1
			y = index-1

			##print(x,y)

			string_list[index] = str(temp_result)

			while x>index and x<len(string_list):
				##print(string_list[x])
				if string_list[x].isnumeric() or string_list[x]=='.':
					#print(string_list[x])
					del(string_list[x])
					#x = x-1
					##print(x)
				#x = x+1	
				else:
					break

			##print(string_list)		

			for i in range(index-1,-1,-1):
				if string_list[i].isnumeric() or string_list[i]=='.':
					del(string_list[i])
					x = x+1
				else:
					break

			

			##print(string_list)

			if len(string_list)	== 1:
				##print('hi')
				return float(string_list[0])
			else:
				string = ''.join(str(elem) for elem in string_list)
				return evaluateString(string)
				
try:
	result = evaluateString('1.1+1.9+4/2-2/2-1')
	if result == -1:
		print('Invalid expression')
	else:
		print(result)

except:
	print("Invalid Expression")

#a,b,c = findOperands(['8.5','*','5.2'],'*')
##print(a,b,c)