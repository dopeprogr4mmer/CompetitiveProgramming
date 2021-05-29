class Node:
	def __init__(self, val):
		self.value = val
		self.next = None
		self.prev = None

class DoublyLinkedList(Node):
	def __init__(self, val):
		super().__init__(val)
		self.head = self
		self.tail = self

	def is_empty(self):
		if self.value == None:
			return True
		return False

	def append(self, val):
		if self.is_empty():
			self.value = val
			self.head = self
			self.tail = self
		else:
			new_node = Node(val)
			#new_node.prev = self.head
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node

	def reverse_parse(self):
		return_list =[]
		temp = self.tail
		return_list.append(temp.value)
		while(temp.prev!=None):
			temp = temp.prev
			return_list.append(temp.value)

		return return_list


	def __str__(self):
		str_list = []
		temp = self.head
		str_list.append(temp.value)
		while(temp.next!=None):
			temp = temp.next
			str_list.append(temp.value)
			#temp = temp.next
		return str(str_list)


"""

l = DoublyLinkedList(1)
l.append(2)
l.append(3)
print(l)
print(l.reverse_parse())

"""

class CircularLinkedList(Node):
	"""docstring for CircularLinkedList"""
	def __init__(self, val):
		super().__init__(val)
		self.head = self
		self.tail = self

	def append(self, val):
		new_node = CircularLinkedList(val)
		#temp.next = new_node
		self.tail.next = new_node
		self.tail = new_node
		self.tail.next = self.head

	def __str__(self):
		return_list = []
		temp = self.head
		return_list.append(temp.value)
		while temp.next!=self.tail.next:
			temp = temp.next
			return_list.append(temp.value)

		return str(return_list)



l = CircularLinkedList(1)
l.append(2)
l.append(3)
l.append(4)
print(l)
print(l.tail.value, l.head.value)