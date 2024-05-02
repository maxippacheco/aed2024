# Escribir una función void three_search (list<int> &L,stack<int> &P); que busca números divisibles por 3 en una lista L y los inserta 
# de manera descendente en una pila P, por lo tanto, luego de ejecutar el algoritmo, al llamar a top() por primera vez,
# obtendremos al menor número encontrado.
from stack_implementation import Stack

def is_divisible_by_three(num):
	if num % 3 == 0: return True
	return False

def three_search(L: list):
	aux = []
	for num in L:
		if is_divisible_by_three(num): aux.append(num)
	
	aux = sorted(aux, reverse=True)
	stack = Stack()
	for num in aux:
		stack.push(num)

	return stack

L = [1,2,3,4,5,6,7,8,9]
sorted_list = three_search(L)

print(sorted_list.top())
