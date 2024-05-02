# Escribir una función void invertm(list<int> &L,int m); que, dada una lista L va invirtiendo los elementos de la lista de a m, ejemplos:
# Ejemplos:
#  	L=[1,2,3,4,5,6,7,8,9,10], m=3  => L=[3,2,1,6,5,4,9,8,7,10]
# 	L=[1,2,3,4,5,6,7,8,9,10], m=4  => L=[4,3,2,1,8,7,6,5,10,9]
# 	L=[1,2,3,4,5,6,7,8,9,10], m=6  => L=[6,5,4,3,2,1,10,9,8,7]

def invertm(L: list, m: int) -> list:
	# step: m
	# 0 to len(l) with step m
	for i in range(0, len(L), m):
		L[i:i+m] = reversed(L[i:i+m])
	return L

# Ejemplos
L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m1 = 3
invertm(L1, m1)
print(L1)
