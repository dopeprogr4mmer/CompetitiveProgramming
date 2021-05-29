class LinkedList:
	def __init__(self, value=None):
		#if value!=None:
		self.value = value
		self.next = None

	def is_empty(self):
		if self.value == None:
			return True
		return False

	def add_node(self, value):
		if self.next == None:
			new_node = LinkedList(value)
			self.next = new_node
		else:
			self.next.add_node(value)

	def parse(self):
		if self.next == None:
			print(self.value)
			return
		else:
			print(self.value)
			self.next.parse()

	def get_length(self):
		temp = self
		count = 1
		while temp.next!=None:
			count+=1
			temp = temp.next
		return count

	def insert(self,index,value):
		if self.get_length()<index:
			return 'nope'
		else:
			i = 0
			temp = self
			while i<index-1:
				temp = temp.next
			new_node = LinkedList(value)
			new_node.next = temp.next
			temp.next = new_node
			#temp.value = value

	def delete(self, value):
		temp = self
		if temp.value == value:
			temp.value = temp.next.value
			temp.next = temp.next.next
			return f'deleted {value}'
		while(temp.value != value and temp.next!= None):
			if temp.next.value == value:
				if temp.next.next == None:
					temp.next = None
				else:
					temp.next = temp.next.next
				return f'deleted {value}'
			else:
				temp = temp.next
		else:
			return "Not in list"



	def __str__(self):
		str_list = []
		temp = self
		str_list.append(temp.value)
		while temp.next != None:
			temp = temp.next
			str_list.append(temp.value)
			#btemp = temp.next
		return str(str_list)

l = LinkedList(7)
print(l.is_empty())
l.add_node(2)
l.add_node(5)
l.get_length()
l.insert(1, 9)
l.add_node(6)
print()
print(l.delete(7))
print(l)
print()
l.parse()
l.get_length()