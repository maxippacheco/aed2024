#  Aplica. Escribir una función applyMap(L,M,ML) que, dada una lista L y una correspondencia M
#  retorna por ML una lista con los resultados de aplicar M a los elementos de L. Si algún elemento
#  de L no está en el dominio de M, entonces el elemento correspondiente de ML no es incluido. Por
#  ejemplo, si L = (1,2,3,4,5,6,7,1,2,3) y M = (1,2),(2,3),(3,4),(4,5),(7,8), entonces, después de
#  hacer applyMap(L,M,ML), debe quedar ML = (2,3,4,5,8,2,3,4).

def apply_map(L, M, ML: dict):
	for i in L:
		if i in M:
			ML.append(M[i])
	return ML

if __name__ == "__main__":    
    L = (1,2,3,4,5,6,7,1,2,3)
    M = {1:2, 2:3,3:4,4:5,7:8}
    ML = []
    print(apply_map(L,M,ML))
