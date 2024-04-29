# Camaleón. Implemente los predicados menor(x, y), mayor(x, y) y dist(x, y) que retornen verdadero 
# si x es menor, mayor o menor en valor absoluto que y respectivamente. Luego implemente una
# función ordena(L, f) que ordene la lista L dependiendo de la función f pasada cómo parámetro.

L = [1, -2, 3, -2, -3, 4, -1, 2, -2, 3, -4, 5]

def menor(x, y):
	return x < y

def mayor(x, y):
	return x > y

def dist(x, y):
	abs(x) < abs(y)

def ordena(L, f):
	for i in range(len(L)):
		for j in range(i+1, len(L)):
			if f(L[i], L[j]):
				aux  = L[i]
				L[j] = L[i]
				L[i] = aux
	return

print(L)
ordena(L, mayor)
print(L)