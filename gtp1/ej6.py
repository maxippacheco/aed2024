# ReemplazaSecuencia. Dada una lista de enteros L y dos listas SEQ y REEMP, posiblemente de
# distintas longitudes, escribir una función reemplaza(L, SEQ, REEMP), que busca todas las secuen
# cias de SEQ en L y las reemplaza por REEMP. Por ejemplo, si L=(1,2,3,4,5,1,2,3,4,5,1,2,3,4,5),
# SEQ=(4,5,1) y REEMP=(9,7,3), entonces después de llamar a reemplaza(L,SEQ,REEMP), debe que
# dar L = (1,2,3,9,7,3,2,3,9,7,3,2,3,4,5). Para implementar este algoritmo primero buscar desde el
# principio la secuencia SEQ, al encontrarla, reemplazar por REEMP, luego seguir buscando a partir del
# siguiente elemento al último de REEMP.

def reemplaza_secuencia(L, SEQ, REEMP):
	i = 0
	while i <= len(L) - len(SEQ):
		if L[i:i + len(SEQ)] == SEQ:
			L[i:i+len(SEQ)] = REEMP
			i += len(REEMP)
		else:
			i += 1

L = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
print(L)
SEQ = [4,5,1]
REEMP = [9,7,3]

reemplaza_secuencia(L, SEQ, REEMP)
print(L)