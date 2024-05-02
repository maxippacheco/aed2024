#  [is-balanced] (stack) Dado un string expr, implementar una función
#  bool is_balanced(string &expr); que determine si el par y orden de {, }, (, ), [, ] está balanceado.
#  Ejemplos:
#  [ ( ) ] { } { [ ( ) ( ) ] ( ) }estábalanceado
#  [ ( ] )noestábalanceado.

from stack_implementation import Stack

def is_balanced(expr: str):
	stack = Stack()
	opening_brackets = {'(', '[', '{'}
	closing_brackets = {')', ']', '}'}
	bracket_pairs = {'(': ')', '[': ']', '{': '}'}

	for char in expr:
		if char in opening_brackets:
			stack.push(char)
		elif char in closing_brackets:
			# hay parentesis de cierre, sin uno de apertura
			if not stack:
				return False
			top_char = stack.pop()
			# si el parentesis de cierre no coincide con el de apertura
			if bracket_pairs[top_char] != char:
				return False
	# si quedan parentesis de apertura sin cerrar, la expresion no esta balanceada
	return not stack
	

# Ejemplos de uso:
expr1 = "[ ( ) ] { } { [ ( ) ( ) ] ( ) }"
expr2 = "[ ( ] )"
print(is_balanced(expr1))  # Output: True
print(is_balanced(expr2))  # Output: False