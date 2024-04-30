# Inverso. Escribir un procedimiento inverso(s) para determinar si una cadena de caracteres de entrada
# es de la forma z=xy donde y es la cadena inversa (o espejo) de la cadena x, ignorando los espacios en
# blanco. Emplear una cola y una pila auxiliares.

from ej3 import Queue
from ej1 import Stack

def inverso(cadena):
  """
  Determina si una cadena es de la forma z = xy, donde y es la inversa de x.

  Parámetros:
    cadena: La cadena de entrada a evaluar.

  Retorno:
    True si la cadena es de la forma z = xy, False en caso contrario.
  """

  # Eliminar espacios en blanco
  cadena = cadena.replace(" ", "")

  # Longitud de la cadena
  longitud = len(cadena)

  # Si la longitud es impar, no puede ser de la forma z = xy
  if longitud % 2 != 0:
    return False

  # Mitad de la longitud
  mitad = longitud // 2

  # Inicializar cola y pila
  cola = Queue()
  pila = Stack()

  # Agregar la primera mitad de la cadena a la cola
  for i in range(mitad):
    cola.push(cadena[i])

  # Agregar la segunda mitad (invertida) a `la pila
  for i in range(mitad - 1, -1, -1):
    pila.push(cadena[i])

  # Comparar caracteres de la cola y la pila
  while not cola.is_empty() and not pila.is_empty():
    if cola.top() != pila.pop():
      return False

  # Si todas las comparaciones son correctas, la cadena es de la forma z = xy
  return True

# Ejemplo de uso
cadena = "noon"
resultado = inverso(cadena)

if resultado:
  print(f"La cadena '{cadena}' es de la forma z = xy")
else:
  print(f"La cadena '{cadena}' NO es de la forma z = xy")
