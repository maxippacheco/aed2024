#  Componentes Conexas. Dado un grafo G encontrar los subconjuntos del mismo D que están desco
#  nectados, es decir, los conjuntos de vértices de cada una de las componentes conexas. Por ejemplo, si
#  G=1−>2,2−>1,3−>4,4−>3,entonces debe retornar D = (1,2,3,4). La signatura de la función
#  a implementar es componentesConexas(G, D).

#### SOLUTION 1 ####
def componentes_conexas(G, D):
	for g in list(G.keys()):
		for d in D:
			if g in d:
				break
			D.append({g})
	return D

#### SOLUTION 2 ####
def componentes_conexas2(G, vertices):
  componentes = []
  for vertice in vertices:
    conectado = False
    for componente in componentes:
        if vertice in componente:
          conectado = True
          componente.append(vertice)
          break
    if not conectado:
      componentes.append([vertice])

### SOLUTION 3 ####
## using recursivity ##
def dfs(G, v, visitados, componente):
    visitados.add(v)
    componente.append(v)
    for vecino in G.get(v, []):
        if vecino not in visitados:
            dfs(G, vecino, visitados, componente)

def componentes_conexas3(G, D):
  visitados = set()
  componentes = []

  for v in D:
      if v not in visitados:
        componente = []
        dfs(G, v, visitados, componente)
        componentes.append(componente)

  return componentes


if __name__ == "__main__":        
    G = {1:[2],2:[1],3:[4],4:[3]}
    D = []
    print("D:",D)