#A Decorator in python is any callable function Python object that is used to modify a function or class.
'''Two types of Decorators
		-Function Decorators
		-Class Decorators
'''

def my_decorator(my_func):
	print("USING DECORATOR")
	return my_func

@my_decorator
def some_func():
	print("Hello from some func")

some_func()

