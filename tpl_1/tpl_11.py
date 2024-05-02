#  list<int> discrete_moving_mean(list<int>& L, int w) que dada una lista de enteros L y un
#  entero w, retorne una lista con los valores de la media móvil con ventana fija de tamaño w. El primer
#  elemento será el promedio (en división entera) de los primeros w elementos de L; el segundo será el
#  promedio desde el 2 elemento al w+1; y en general, el elemento en la posición N de la lista resultado, será
#  el promedio entre los elementos [N,w+N) de L.
#  Ejemplos:
#  Para L: [1,2,6,5,8,3,4,6] y w=2 debe retornar [1,4,5,6,5,3,5]
#  Para L: [1,2,6,5,8,3,4,6] y w=3 debe retornar [3,4,6,5,5,4]
#  Para L: [1,2,6,5,8,3,4,6] y w=4 debe retornar [3,5,5,5,5]

def discrete_moving_mean(L: list, w: int):
	result = []
	sum_window = sum(L[:w])

	result.append(sum_window // w)

	for i in range(w, len(L)):
		sum_window += L[i] - L[i - w]
		result.append(sum_window // w)
	return result

# Ejemplos de uso
L1 = [1, 2, 6, 5, 8, 3, 4, 6]
w1 = 2
print("Para L1:", L1, "y w1 =", w1, "debe retornar", discrete_moving_mean(L1, w1))

L2 = [1, 2, 6, 5, 8, 3, 4, 6]
w2 = 3
print("Para L2:", L2, "y w2 =", w2, "debe retornar", discrete_moving_mean(L2, w2))

L3 = [1, 2, 6, 5, 8, 3, 4, 6]
w3 = 4
print("Para L3:", L3, "y w3 =", w3, "debe retornar", discrete_moving_mean(L3, w3))
