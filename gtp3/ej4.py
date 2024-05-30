#  mergeMap. Dadas dos correspondencias A y B, que asocian enteros con listas ordenadas de enteros,
#  escribir una función mergeMap(A,B,C) que devuelve en C una correspondencia que asigna al elemento
#  x la fusión ordenada de las dos listas A[x] y B[x]. Si x no es clave de A, entonces C[x] debe ser B[x] y
#  viceversa. Sugerencia: utilice la función merge implementada en uno de los ejercicios anteriores.

def merge_map(A, B):
	C = {}

	all_keys = set(A.keys()).union(set(B.keys()))

	for key in all_keys:
		if key in A and key in B:
			# Fusionar las listas de A[key] y B[key] y ordenarlas
			C[key] = sorted(A[key] + B[key])
		elif key in A:
			# Solo A tiene la key
			C[key] = A[key]
		elif key in B:
			# Solo B tiene la key
			C[key] = B[key]
		
	return C

# Ejemplo de uso
A = {
    1: [1, 3, 5],
    2: [2, 4, 6],
    3: [7, 8]
}

B = {
    2: [1, 3, 5],
    3: [9, 10],
    4: [11, 12]
}

C = merge_map(A, B)
print(C)