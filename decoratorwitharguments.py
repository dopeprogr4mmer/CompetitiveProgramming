import functools     #for higher order functions
def trace(func):
	"""As a best practice it is recommended to use functools.wraps in all self written decorators"""
	@functools.wraps(func)      #carries over docstring and other metadata of the input function like doc and name
	def wrapper(*args, **kwargs):
		"""wrapper doc"""
		print(f'TRACE: Calling {func.__name__}() with {args}, {kwargs}')
		original_result = func(*args, **kwargs)
		print(f'TRACE: {func.__name__}() returned {original_result!r}') 

		return original_result
	return wrapper

@trace			#shorthand for calling the decorator same as 'say = trace(say)'
def say(name, line):
	"""docstring"""
	return f'{name}: {line}'

print(say.__doc__)
print(say.__name__)
print(trace.__doc__)
s = say('Phantom', line="Welcome to PhantomZone!")
print(s)