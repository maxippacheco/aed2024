#  BasicSort. Escribir una función basicsort(L), que ordena los elementos de L de menor a mayor. Para
#  ello emplear el siguiente algoritmo simple: utilizando una lista auxiliar L2, tomar el menor elemento de
#  L, eliminarlo de L e insertarlo al final de L2 hasta que L esté vacía. Luego copiar L2 en L

def basic_sort(L: list):
	L2: list = []
	while L:
		min_element = min(L)
		L.remove(min_element)
		L2.append(min_element)
	
	for element in L2:
		L.append(element)

	return L


L = [ 2, 1, 4, 7, 9, 10]

ordered_list = basic_sort(L)
print(ordered_list)
