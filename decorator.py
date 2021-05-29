def modify(func):
	def wrapper():
		call = func()
		return call.upper()
	return wrapper

@modify
def greet():
	return 'hello'

#greeting = greet()
#print(greeting)

'''
print(greet())
greet = modify(greet)
print(greet())
'''

#Adding multiple decorators to functions
#Nested decorators
def strong(func):
	def wrapper():
		call = func()
		return '<strong>'+call+'</strong>'
	return wrapper

def emphasis(func):
	def wrapper():
		call = func()
		return '<em>'+call+'</em>'
	return wrapper

@strong
@emphasise
def greeting():
	return 'hello'

#decorated_greet = strong(emphasis(greet))
#print(decorated_greet)
greet = greeting()
print(greet)