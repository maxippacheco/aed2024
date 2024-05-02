#  Implemente la función list<int> sum_sublist(list<int>& L,int S) que dada una lista de enteros L
#  y un entero S, encuentre y retorne una sublista cuya suma sea S. Si no existe ninguna sublista con dicha
#  suma, retorne una lista vacía. En caso de haber varias listas que cumplan retorne la primera y la más
#  corta.
#  Ejemplos:
#  Para L: [1,2,6,5,8,3,4,6] y S=13 debe retornar [2,6,5]
#  Para L: [1,2,6,5,8,3,4,6] y S=15 debe retornar [8,3,4]
#  Para L: [1,2,6,5,8,3,4,6] y S=17 debe retornar []


def sum_sublist(L, s):
	result = []
	current_sum = 0

	for num in L:
		result.append(num)
		current_sum += num

		while current_sum > s:
      # Si excede, eliminar elementos del inicio de la lista resultante
			current_sum -= result.pop(0)
		
		if current_sum == s:
			return result[:]
		
	return []

L1 = [1,2,6,5,8,3,4,6]
S1 = 13
print("Para L1:", L1, "y S1 =", S1, "debe retornar", sum_sublist(L1, S1))
