def add_names(names, aggregate_list = []):  			#if aggregate_list = []. Does not reassign
	'''if isinstance(aggregate_list, type(None)):		#if aggregate_list = None. Reassign!
		aggregate_list = []'''

	for name in names:
		aggregate_list.append(name)

	return aggregate_list 

if __name__ == '__main__':
	print(add_names(['rohan','rima','rahul']))
	print(add_names(['roshan','riyaz','romeo']))