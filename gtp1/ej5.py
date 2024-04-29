# Junta. Escribir una función junta(L, c) que, dada una lista L, agrupa de a c elementos, dejando su
# suma in-place. Por ejemplo, si se le pasa como argumento la lista L = (1,3,2,4,5,2,2,3,5,7,4,3,2,2),
# después de aplicar el algoritmo junta(L,3) debe quedar L = (6,11,10,14,4) (notar que se agrupan
# los últimos elementos, pese a no completar los tres requeridos). El algoritmo debe tener un tiempo de
# ejecución O(n).

def junta(L, c):
  i = 0
  while i < len(L):
    L[i:i+c] = [sum(L[i:i+c])]
    i += 1
  return L


# Example usage
L = [1, 3, 2, 4, 5, 2, 2, 3, 5, 7, 4, 3, 2, 2]
junta(L, 3)
print(L)  # Output: [6, 11, 10, 14, 4]
