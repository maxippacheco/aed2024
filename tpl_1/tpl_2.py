# Escribir una función void concatsz(list<list<int>> &LL,list<int> &L); que, dada una lista de lista de enteros LL, los concatena en
# una sola lista L, colocando primero los elementos de la lista más larga, luego los de la segunda más larga y así siguiendo. 
# Si hay listas con la misma longitud deben quedar en el orden que estaban en la lista original (estabilidad). 
from typing import List

def sort_sublist(LL: List[List[int]]):
	return sorted(LL, key=len, reverse=True)

def concatsz(LL: List[List[int]], L: List[int]):
	LL = sort_sublist(LL)

	for sublists in LL:
		L.extend(sublists)

	return L

L = []
sublists = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10], [13, 14], [11, 12], [15]]
sorted_sublists = concatsz(sublists, L)
print(sorted_sublists)
