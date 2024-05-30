#  Dijkstra. Programe Dijkstra( G, u, v, path) quedadoelgrafoponderado GdefinidocomographW,
#  implemente el algoritmo de Dijkstra para retornar el costo del camino más corto entre el vértice de
#  partida u y el vértice de llegada v. Además debe devolver en path uno de los posibles caminos. Si no
#  hay camino posible, retornar un número muy grande (infinito).

#Weighted Graph
GW = {
  'a':{'b':16,'c':10,'d':5},
  'b':{'a':16,'c':2,'f':4,'g':6},
  'c':{'a':10,'b':2,'d':4,'e':10,'f':12},
  'd':{'a':5,'c':4,'e':15},
  'e':{'c':10,'d':15,'f':3,'z':5},
  'f':{'b':4,'c':12,'e':3,'g':8,'z':16},
  'g':{'b':6,'f':8,'z':7},
  'z':{'e':5,'f':16,'g':7}
}

def dijkstra(GW, u, v, path):
	# D a cada vertice su costo candidato
	D = {}
	# P a cada vertice su camino candidato
	P = {}

	vert_pendientes = list(GW.keys())
	vertices_procesados = []

	# inicializamos
	for k in GW.keys():
		D[k] = 100000
		P[k] = []

	D[u] = 0
	P[u] = [u]

	print(D)

	while vert_pendientes:
		# buscamos el menor costo entre los pendientes
		curr_min = 100000
		for vc in vert_pendientes:
			if D[vc] < curr_min:
				curr_min = D[vc]
				curr_vert = vc
		
		# comparamos el costo candidato del vertice adyacente
		# con el costo de llegarle desde el vertice actual

		for adj in GW[curr_vert]:
			if D[adj] > D[curr_vert] + GW[curr_vert][adj]:
				D[adj] = D[curr_vert] + GW[curr_vert][adj]
				P[adj] = P[curr_vert] + [adj]

		vert_pendientes.remove(curr_vert)
		vertices_procesados += [curr_vert]
		print('Procesados: '+ str(vertices_procesados))
		print(D)
		path[:] = P[v]
    

path = []
dijkstra(GW,'a','z',path)
print(path)
    