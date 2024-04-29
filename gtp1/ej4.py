# Invierte.
# Escribir una función invert(L), que invierte el orden de la lista L. Este algoritmo debe
# implementarse in place y debe ser O(n). Restricción: no utilizar el método len. 
# Implementar aplicando:
#  a) programación recursiva

def sort_recursive(lista, start, end):
  """
  Función recursiva que invierte el orden de una lista.
  """
  if start < end:
    lista[start], lista[end] = lista[end], lista[start]
    sort_recursive(lista, start + 1, end - 1)

def sort(lista):
  """
  Función que invierte el orden de una lista usando recursión.
  """
  sort_recursive(lista, 0, len(lista) - 1)
  return lista


# Ejemplo de uso
L = [1, 2, 3, 4, 5]
sort(L)
print(L)  # Output: [5, 4, 3, 2, 1]


#  b) list comprehension
def sort_list_comprehension(L: list):
	new_list = L.reverse()
    
	return new_list

# Ejemplo de uso
L = [1, 2, 3, 4, 5]
sort_list_comprehension(L)
print(L)  # Output: [5, 4, 3, 2, 1]
