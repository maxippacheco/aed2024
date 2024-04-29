# Problema de Josephus. Un grupo de soldados se halla rodeado por una fuerza enemiga. No hay
# esperanzas de victoria si no llegan refuerzos y existe solamente un caballo disponible para el escape.
# Los soldados se ponen de acuerdo en un pacto para determinar cuál de ellos debe escapar y solicitar
# ayuda. Forman un círculo y se escoge un número n al azar. Igualmente se escoge el nombre de un soldado.
# Comenzando por el soldado cuyo nombre se ha seleccionado, comienzan a contar en la dirección del
# reloj alrededor del círculo. Cuando la cuenta alcanza el valor n, este soldado es retirado del círculo y la
# cuenta comienza de nuevo, con el soldado siguiente. El proceso continúa de tal manera que cada vez que
# se llega al valor de n se retira un soldado. El último soldado que queda es el que debe tomar el caballo
# y escapar. Entonces, dados un número n y una lista de nombres, que es el ordenamiento en el sentido
# de las agujas del reloj de los soldados en el círculo (comenzando por aquél a partir del cual se inicia la
# cuenta), escribir un procedimiento josephus(nombres,n) que retorna una lista con los nombres de los
# soldados en el orden que han de ser eliminados y en último lugar el nombre del soldado que escapa.

nombres = ["Miguel", "Juan", "Tomas", "Jose", "Rene", "Santiago", "Benjamin", "Milton"]
n = 7

def josephus(nombres: list, n: int):
	aux = nombres.copy()
	sorteoAux = []
	idx = 0

	while len(aux) != 0:
		idx = (idx + n-1) % len(aux)
		elim = aux.pop(idx)
		sorteoAux.append(elim)
	
	return sorteoAux

sorteo = josephus(nombres,n)
print("Lista: ", nombres)
print("Sorteo: ", sorteo)