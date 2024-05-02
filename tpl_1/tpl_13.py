#  [merge-kway] (cola)
#  Implementar una función void merge_kway(vector< queue<int> > &qords,queue<int> &merged)
#  que dado un vector de colas ordenadas ordqs, obtener la cola merged resultante de la fusión de todas
#  las colas en una sola, de forma de que los elementos siguen ordenadas. Por ejemplo si
#  ordqs=((1,3,5,6),(0,3,5,8),(6,9,10)) entonces debe dar merged=(0,1,3,3,5,5,6,6,8,9,10). El
#  algoritmo puede ser destructivo sobre ordqs.

from queue_implementation import Queue

# todo revisar
def merge_kway(qords, merged):
	all_elements = Queue()
	for q in qords:
		while not q.is_empty():
			all_elements.append(q.pop())
	
	all_elements.sort()

	for element in all_elements:
		merged.push(element)

# Ejemplo de uso:
# ordqs = [Queue([1,3,5,6]), Queue([0,3,5,8]), Queue([6,9,10])]
# merged = Queue([])
# merge_kway(ordqs, merged)

# # Imprimir el elemento superior de la cola fusionada
# print(merged.top())
