# Clase stack: Implementar la clase stack que implementa una pila a partir de nodos enlazados. 

class Empty(Exception):
	pass

class Node:
	def __init__(self, data, next) -> None:
		self._data = data
		self._next = next

class Stack:
	def __init__(self) -> None:
		self._head = None
		self._size = 0

	def __len__(self):
		return self._size
	
	def is_empty(self):
		if self._size == 0:
			return True
		else: return False

	def push(self, data):
		if self._size == None:
			self._head = Node(data, self._head)
		else:
			new_node = Node(data, self._head)
			self._head = new_node
		self._size += 1
	
	def pop(self):
		if self.is_empty():
			raise(Empty("Empty stack"))
		answer = self._head._data
		self._head = self._head._next
		self._size -= 1
		# answer is only created to show which element was deleted
		return answer

	def top(self):
		return self._head._data
	
def destructive_print(s):
  L = []
  while len(s) > 0:
    L.append(s.pop())
  print(L)
        