def rotacion(C):
  """
  Rota la cola C hasta que un número par quede al frente.

  Parámetros:
    C (lista): La cola de enteros.

  Retorno:
    lista: La cola rotada con un número par al frente.
  """
  while C[0] % 2 != 0:
    C.append(C.pop(0))
  return C

cola = [1, 3, 5, 2, 4]
cola_rotada = rotacion(cola)
print(cola_rotada)  # Salida: [2, 4, 1, 3, 5]
