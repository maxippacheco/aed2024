#  Camino. Implemente el predicado esCamino(G, L) que recibe una lista L y determina si es o no
#  camino en el grafo G. El grafo se representa como un mapa que relaciona cada vértice (clave) con la
#  lista de sus vértices adyacentes (valor).

def es_camino(G, L):
	if len(L) < 2:
		return False # Un camino debe tener al menos dos vertices
	
	for i in range(len(L) - 1):
		origen = L[i]
		destino = L[i + 1]
		if destino not in G.get(origen, []): # Verifica si hay una arista del origen al destino
			return False

	return True

def es_camino2(G,L):
  # except for the last one, because we're comparing each vertex with the next one.
    for i in range(len(L)-1):
        print(L[(i+1)%len(L)])
        print(G[L[i%len(L)]])
        if L[(i+1)%len(L)] not in G[L[i%len(L)]]:
            return False
    return True



if __name__ == "__main__":    
    L = [1,2,3,4,5,1,2,3]
    G = {1:[2,5],2:[3],3:[2,4],4:[3,5],5:[4,1]}    
    print("Es Camino:", es_camino2(G,L))