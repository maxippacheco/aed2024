# map2list. Escribir una función que dado un mapa (diccionario) M retorna las listas de claves y valores.
# Ejemplo: si M={1->2, 3->5, 8->20}, entonces debe retornar Keys = [1,3,8] y Vals = [2,5,20]

def map2list(dictionary: dict):
	keys = []
	vals = []

	for key, val in dictionary.items():
		keys.append(key)
		vals.append(val)

	return keys, vals

M = {
	1: 2,
	3: 5,
	8: 20
}

keys, vals = map2list(M)

print(keys)
print(vals)