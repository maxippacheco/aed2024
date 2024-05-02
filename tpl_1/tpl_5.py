# Escribir una función void evensublist(list<int> &L,list<int> &subl); que retorna la sublista más larga de L 
# que contenga todos elementos pares. 

# Ejemplo:
# L=[7,8,3,4,6,2,0,3,4,1,5,5,5,10,5,9,0,2,7,4,6,3]
#    => subl=[4,6,2,0]
# En caso de que hubiere dos listas con igual longitud debe considerarse la que empieza primero, es decir la que está 
# más cerca del comienzo de la lista. 

# Ayuda:
# Recorrer todos los elementos con un iterador p
# A partir de ese iterador construir la lista con todos elementos pares a partir de p
# Ir manteniendo en subl la lista de mayor longitud. 

def list_is_even(L: list):
	for num in L:
		if num % 2 != 0:
			return False
	return True

def evensublist(L: list):
	max_sublist = []

	for i in range(len(L)):
		for j in range(i+1, len(L)+1):
			sublist = L[i:j]
			if list_is_even(sublist) and len(sublist) > len(max_sublist):
				max_sublist = sublist
	return max_sublist
	
L=[7,8,3,4,6,2,0,2,4,1,5,5,5,10,5,9,0,2,7,4,6,3]
max_subl = evensublist(L)
print(max_subl)