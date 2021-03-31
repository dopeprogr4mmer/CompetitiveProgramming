"""
Refactoring a piece of code
"""
def get_answer(prompt):
	"""
	Optimising  a piece of code
	Getting rid of duplication
	""" 
	while True:
		answer = input(prompt).strip().lower()
		if answer in ('yes','no'):
			return answer

answer = get_answer('Yes or No?')
print(answer)