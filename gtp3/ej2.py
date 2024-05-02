# list2map. Escribir una función que dadas las listas de claves Keys = [k1,k2,k3, ...] y valores Vals,
# [v1,v2,v3, ...] retorna el diccionario M con las asignaciones correspondientes {k1->v1, k2->v2,
# k3->v3, ...}. Utilice la signatura list2map(M, Keys, Vals).

def list2map(keys: list, values: list):
	if len(keys) == len(values):
		aux = {}
		for key, value in zip(keys, values):
			aux[key] = value
		
		return aux
	else:
		raise Exception("Both lists do not have the same length")

# Ejemplo de uso
Keys = ['k1', 'k2', 'k3']
Vals = ['v1', 'v2', 'v3']
resultado = list2map(Keys, Vals)
print(resultado)
