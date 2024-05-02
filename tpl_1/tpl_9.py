# [reverse-stack] Escribir un programa que invierta una pila S utilizando recursión. No está permitido el
# uso de constructores iterativos (while, for, etc) ni tampoco el uso estructuras de datos adicionales. Sólo
# pueden utilizarse métodos de la pila, a saber:
# 		S.empty()
#  		S.top()
#  		S.push(s)
#  		S.pop()
# Se propone el siguiente algoritmo recursivo:
# 	Si la pila está vacia finalizar
# Si no:
# 	• Guardar una copia del elemento al tope
#  	• Quitarlo de la pila
#  	• Invertir el resto de la pila
#  	• Insertar el elemento guardado al final de la lista invertida
# Para el último paso se requiere un método auxiliar, también recursivo, que reciba una lista e inserte un
# elemento en la base de la misma, siguiendo el siguiente algoritmo:
# Si la pila está vacía, insertar el elemento.
# Si no:
#  	• Almacenar una copia del elemento al tope
#  	• Quitarlo de la pila
#  	• Insertar el elemento recibido al final de la pila restante
#  	• Apilar el temporal en la pila resultado

from stack_implementation import Stack

def insert_at_bottom(stack: Stack, item):
    # Check if the stack is empty. If it's empty, it means we've reached the bottom of the stack.
		if stack.is_empty():
        # If the stack is empty, simply push the item onto the stack.
			stack.push(item)
		else:
      # If the stack is not empty, we need to recursively remove elements and push them back
      # onto the stack until we reach the bottom.
        
      # 1. Store a copy of the top element of the stack.
			temp = stack.top()
      # 2. Remove the top element from the stack.
			stack.pop()
    	# 3. Recursively insert the item at the bottom of the stack.
			insert_at_bottom(stack, item)
      # 4. Push back the original top element onto the stack.
			stack.push(temp)

def reverse_stack(stack):
    # Base case: if the stack is not empty, proceed with the reversal process.
    if not stack.empty():
        # 1. Store a copy of the top element of the stack.
        temp = stack.top()
        # 2. Remove the top element from the stack.
        stack.pop()
        # 3. Recursively reverse the remaining elements of the stack.
        reverse_stack(stack)
        # 4. Insert the stored top element at the bottom of the reversed stack.
        insert_at_bottom(stack, temp)



# Ejemplo de uso
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0

    def top(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

# Crear una pila
S = Stack()
S.push(1)
S.push(2)
S.push(3)
S.push(4)

# Imprimir la pila original
print("Pila original:", S.items)

# Invertir la pila
reverse_stack(S)

# Imprimir la pila invertida
print("Pila invertida:", S.items)
