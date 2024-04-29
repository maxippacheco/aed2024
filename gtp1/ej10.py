# Palíndromo. Escribir un predicado es_palindromo(S), que reciba como parámetro una cadena de
# texto S y determine si ésta es un palíndromo, ignorando los espacios entre palabras. Un palíndromo es
# una secuencia de caracteres que se lee igual hacia adelante que hacia atrás, por ejemplo: alli si maria
# avisa y asi va a ir a mi silla. Recordar que un string puede indexarse como un vector. Con el fin de
# utilizar la estructura <list>, primero deben pasarse los elementos del string a una lista y solo utilizar
# ésta en el algoritmo.

def es_palindromo(s: str):
	s = s.replace(' ', '')

	if s == s[::-1]:
		return True
	else:
		return False
	
s = "alli si maria avisa y asi va a ir a mi silla"
print("Es palindromo? ", es_palindromo(s))