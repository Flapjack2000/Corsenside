class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		node = Node(data)
		node.next = self.head
		self.head = node

	def insert_in_middle(self, index: int, data):
		if index >= len(self):
			raise IndexError
		elif index == 0:
			self.insert_at_beginning(data)
		else:
			curr_node = self.head
			for i in range(index-1):
				curr_node = curr_node.next
			node = Node(data)
			node.next = curr_node.next
			curr_node.next = node

	def insert_at_end(self, data):
		if self.head is None:
			self.insert_at_beginning(data)
		else:
			curr_node = self.head
			while curr_node.next:
				curr_node = curr_node.next
			node = Node(data)
			curr_node.next = node

	def delete_at_index(self, index: int):
		if index >= len(self):
			raise IndexError
		else:
			curr_node = self.head
			for i in range(index - 1):
				curr_node = curr_node.next
			curr_node.next = curr_node.next.next

	def __len__(self):
		count = 0
		curr_node = self.head
		while curr_node is not None:
			curr_node = curr_node.next
			count += 1
		return count

	def __str__(self):
		string = ""
		curr_node = self.head
		while curr_node:
			string += f"{curr_node.data} -> "
			curr_node = curr_node.next
		string += "None"
		return string

	def __repr__(self):
		return self.__str__()
