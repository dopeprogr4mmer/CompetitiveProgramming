class Tree:
	def __init__(self, initval=None):
		self.value = initval
		if self.value:
			self.right = Tree()
			self.left = Tree()
			print('sjfd')
		else:
			self.right = None
			self.left = None
			print('snfndj')

	def is_empty(self):
		if self.value == None:
			return True
		return False

	def is_root(self):
		if self.left == None and self.right == None:
			return True
		return False

	def minval(self):
		if self.left.is_empty():
			return self.value
		return self.left.minval()

	def maxval(self):
		if self.right.is_empty():
			return self.value
		return self.right.maxval()

	def make_empty(self):
		self.value = None
		self.left = None
		self.right = None

	def copy_right(self):
		self.value = self.right.value
		self.left = self.right.left
		self.right = self.right.right

	def find(self, val):
		if self.is_empty():
			return False

		if self.value == val:
			return True

		if val<self.value:
			return self.left.find(val)

		if val>self.value:
			return self.right.find(val)



	def insert(self, val):
		if self.is_empty():
			self.value = val
			self.right = Tree()
			self.left = Tree()
			return "hola"
		
		if self.value == val:
			return 

		if val<self.value:
			self.left.insert(val)
			print('left')
			return
			
		if val>self.value:
			self.right.insert(val)
			print('right')
			return

	def delete(self, val):
		if self.is_empty():
			#print('j')
			return f'{val} not in tree'

		if val<self.value:
			return self.left.delete(val)


		if val>self.value:
			return self.right.delete(val)

		if val == self.value:
			if self.is_root():
				self.make_empty()
			if self.left.is_empty():
				self.copy_right()
			else:
				self.value = self.left.maxval()
				self.left.delete(self.left.maxval())

		return f'{val} deleted'

	def inorder(self):
		if self.is_empty():
			return ([])
		else:
			return (self.left.inorder() + [self.value] +self.right.inorder())

	def preorder(self):
		if self.is_empty():
			return []
		return [self.value] +self.left.preorder() + self.right.preorder()

	def postorder(self):
		if self.is_empty():
			return []
		return self.left.postorder() + self.right.postorder() + [self.value]

	def levelorder(self):
		pass

	def __str__(self):
		return str(self.postorder())



t = Tree()
print(t.insert(2))
t.insert(4)
t.insert(3)
t.insert(1)
print(t)
print(t.maxval())
print(t.minval())
print(t.find(2), t.find(7))
print(t.delete(10))