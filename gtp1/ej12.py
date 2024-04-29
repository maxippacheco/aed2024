# maxSubList. Programar una función maxsublist(L) la cual reciba una lista de enteros y encuentre
# y retorne la sublista Lmax que obtenga la mayor suma entre todos sus elementos. Notar que debido
# a que algunos elementos pueden ser negativos el problema no se resuelve simplemente tomando todos
# los elementos. También es posible que la sublista resultado no contenga ningún elemento, en el caso
# de que todos los elementos de L sean negativos. Si hay varias sublistas que den la misma suma, debe
# retornar la que comience primero y sea más corta. Por ejemplo: [1,2,-5,4,-3,2]->[4], [5,-3,-5,1,7,-2]->[1,7],
# [4,-3,11,-2]->[4,-3,11].

def max_sublist2(L):
  sub = L[0:1]
  for i in range(len(L)):
    for j in range(len(L)):
      if sum(L[i:j]) > sum(sub):
        sub = L[i:j]
  return sub

def max_sublist(L: list[int]):
	aux = []
	for i in range(len(L)):
		for j in range(len(L)):
      # Check if the current sublist has a higher sum than the current maximum
			if sum(L[i:j]) > sum(aux):
				aux = L[i:j]
      # If the current sublist has the same sum as the maximum:			
			elif sum(L[i:j]) >= sum(aux):
        # Only update if the current sublist has fewer elements (shorter)
				if len(L[i:j]) < len(aux):
					continue
				else:
					# Update the maximum sublist if it has the same sum but is shorter					
					aux = L[i:j]
	return aux

test = [[2,2,-5,4,-3,2], [5,-3,-5,1,7,-2], [4,-3,11,-2]]

result = [max_sublist(tc) for tc in test]
print(result)