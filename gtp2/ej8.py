# SortQueue. Escribir una función sort(L), que ordena los elementos de L de menor a mayor. Para ello
# utilizar el siguiente algoritmo simple, utilizando una cola auxiliar C: ir tomando el menor elemento de
# L, eliminarlo de L e insertarlo en C hasta que L este vacía. Luego insertar los elementos de C en L.

from ej3 import Queue

def sort(data: list):
	P = Queue()	
	Q = Queue()
	
	while data:
			m = min(L)
			data.remove(m)
			P.push(m)
			Q.push(m)
	
	
	while len(P) > 0:
			data.insert(0,P.pop())
			
	M = []
	while len(Q) > 0:
			M.append(Q.pop())
	return M