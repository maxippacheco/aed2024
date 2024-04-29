# Compacta. Escribir una función compacta(L, S) que toma un elemento entero n de S y, si es positivo,
# saca n elementos de L y los reemplaza por su suma. Esto ocurre con todos los elementos de S hasta que
# se acaben, o bien se acaben los elementos de L.

def compacta(L: list, S: list) -> list:
	for i in range(len(S)):
		L[i:i+S[i]] = [sum(L[i:i+S[i]])]
	return L

L  = [2,2,2,2,2,2,2,2,2,2,2,2]
S = [3,2,3,2,5]

print("Lista original: ", L)
print("Lista compacta: ", compacta(L,S))