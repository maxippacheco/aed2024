#  Distancia. Dado un grafo G y un vértice de partida x se desea determinar la distancia éste al resto de
#  los vértices en G. Se solicita retornar una estructura de capas de vecinos de G alrededor de x definida
#  de la siguiente forma: la capa 0 es x, la capa 1 son los vecinos de x. A partir de allí la capa n ≥ 2 está
#  formada por los vecinos de los vértices de la capa n−1 (es decir la adyacencia de la capa) pero que no
#  están en las capas anteriores (en realidad basta con verificar que no estén en las capas n−1 ni n−2).
#  Notar que los vértices en la capa n se encuentran a una distancia n del vértices de partida.

def distancia(G, v):
	L = list(G.keys())
	D = {}
	D[0] = [v]
	L.remove(v)

	D[1] = G[v]
	for i in G[v]:
		L.remove(i)

	for i in D[1]:
		if i in L:
			L.remove(i)

	level = 2
	while L:
		D[level] = []
		for i in D[level - 1]:
			for j in G[i]:
				if j not in D[level - 1] and j not in D[level - 2] and j not in D[level]:
					D[level].append(j)
					if j in L:
						L.remove(j)
			level += 1
	return D        

if __name__ == "__main__":
    
    G = {0:[1,2,3],1:[0,2,4],2:[0,1,3,4],3:[0,2],4:[1,2]}
    dist = distancia(G, 1)
    