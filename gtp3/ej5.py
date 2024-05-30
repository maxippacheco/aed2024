#  cutoffMap. Implemente una función cutoffMap(M, p, q) que elimina todas las claves que NO están
#  en el rango [p,q). En las asignaciones que quedan también debe eliminar los elementos de la lista que
#  no están en el rango. Si la lista queda vacía entonces la asignación debe ser eliminada. Por ejemplo:
#  si M =1−>(2,3,4),5− > (6,7,8),8− > (4,5),3− > (1,3,7), entonces cutoffMap(M,1,6) debe dejar
#  M =1−>(2,3,4),3− >(1,3). Notar que la clave 5 ha sido eliminada si bien está dentro del rango
#  porque su lista quedaría vacía. Restricciones: el programa no debe usar contenedores auxiliares

def cut_off_map(M, p, q):
	keys = list(M.keys())

	for key in keys:
		if key < p or key >= q:
			del M[key]
			continue
		else:
			for val in list(M[key]):
				if val < p or val >= q:
					M[key].remove(val)
		if M[key] == []: del M[key]
	
	return M

if __name__ == "__main__":    
    M = {}
    M[1] = [2,3,4]
    M[5] = [6,7,8]
    M[8] = [4,5]
    M[3] = [1,3,7]
    print(cut_off_map(M,1,6))
