# Ascendente. Escribir una función ascendente(L, LL) que, dada una lista L, la subdivide (manteniendo 
# el orden de los elementos de la lista original) y produce una lista de listas LL de tal forma de
# que cada sublista es ascendente

def ascendente(L, LL):
	sublist = []
	prev_el = 0

	for current_element in L:
		if current_element > prev_el:
			sublist.append(current_element)
			prev_el = current_element
		else:
			LL.append(sublist)
			sublist = []
			sublist.append(current_element)
			prev_el = current_element
	LL.append(sublist)

L = [1,2,3,2,3,4,1,2,2,3,4]
LL = []
ascendente(L, LL)
print(L)
print(LL)