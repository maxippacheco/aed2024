# SortStack. Escribir una función sort(L), que ordena los elementos de L de mayor a menor. Para ello
# emplear el siguiente algoritmo simple, utilizando una pila auxiliar P: ir tomando el menor elemento de
# L, eliminarlo de L e insertarlo en P hasta que L este vacía. Luego insertar los elementos de P en L.

from ej1 import Stack

def sort(data: list) -> None:
	stack = Stack()

	while data:
		min_el = min(data)
		data.remove(min_el)
		stack.push(min_el)

	while stack:
		data.append(stack.pop())

	return data

lista_desordenada = [5, 2, 4, 1, 3]
print(f"Lista desordenada: {lista_desordenada}")
lista_ordenada = sort(lista_desordenada)
print(f"Lista ordenada: {lista_ordenada}")
