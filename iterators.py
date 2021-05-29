# Here is an example of a python inbuilt iterator
# value can be anything which can be iterate
iterable_value = 'Geeks'
iterable_obj = iter(iterable_value)
"""
__iter(iterable)__ method that is called for the initialization of an iterator. 
This returns an iterator object
"""

while True:
	try:

		# Iterate by calling next
		item = next(iterable_obj)
		print(item)
	except StopIteration:
		"""
		next ( __next__ in Python 3) The next method returns the next value for the iterable. 
		When we use a for loop to traverse any iterable object, internally it uses the 
		iter() method to get an iterator object which further uses next() method to iterate over.
		This method raises a StopIteration to signal the end of the iteration.
		"""

		# exception will happen when iteration will over
		break
