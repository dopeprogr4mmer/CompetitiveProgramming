import timeit 

my_setup = "from math import sqrt"

my_code = '''
			def example():
				mylist = []
				for x in range(10000):
					mylist.append(sqrt(x))
			'''

print(timeit)

timeit.timeit("print('hello')")