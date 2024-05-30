# InverseMaps. Dos correspondencias M1 y M2 son inversas una de la otra si tienen el mismo número
# de asignaciones y para cada par de asignación x → y en M1 existe el par y → x en M2. Escribir un
# predicado areinverse(M_1, M_2) que determina si las correspondencias M1 y M2 son inversas.

def are_inverse(M1, M2):
	if len(M1) != len(M2):
		return False
	
	for key, value in M1.items():
		if M2.get(value) != key:
			return False
	
	for key, value in M2.items():
		if M1.get(value) != key:
			return False
	
	return True

M1 = {'a': 1, 'b': 2, 'c': 3}
M2 = {1: 'a', 2: 'b', 3: 'c'}

print(are_inverse(M1, M2))