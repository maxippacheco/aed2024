# Chequeo. Escribir un segmento de programa que lea expresiones aritméticas del estilo ((a- b)*(5- c))/4 y 
# verifique si los paréntesis están embebidos correctamente. Es decir, debemos verificar si:
# a) Existe igual número de paréntesis a izquierda y derecha;
# b) Cada paréntesis de la derecha está precedido de su correspondiente paréntesis a la izquierda

def chequeo(expresion):
  stack = []
  left_counter = 0
  right_counter = 0

  for char in expresion:
    if char == "(":
      stack.append(char)
      left_counter += 1
    elif char == ")":
      if not stack:
        return False
      stack.pop()
      right_counter += 1

  return left_counter == right_counter and not stack
	
expresion = '(a)'
resultado = chequeo(expresion)

if resultado:
    print("Los paréntesis están embebidos correctamente.")
else:
    print("Los paréntesis no están embebidos correctamente.")
