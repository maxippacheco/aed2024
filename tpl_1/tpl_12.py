# [Pareto] (lista)
#  Se dice que un punto x = (x1 x2 xn) n-dimensional domina a otro punto y = (y1 y2 yn) si se
#  cumple que:
#  k [1n] :xk yk y k0 [1n] xk0 <yk0 (1)
#  Por ejemplo x=[2,1,5] domina a y=[2,2,5], pero dado z=[1,2,5] no es cierto ni que x domina a z ni z
#  domina a x.
#  Entonces, dada una lista de puntos de coordenadas enteras positivas list<vector<int>> L,
#  implemente una función list<vector<int>> Pareto(list<vector<int>>&L); que retorne la lista de
#  puntos no-dominados (aquellos que no son dominados por ningún otro punto). Se garantiza que cada
#  vector<int> tiene n coordenadas. La lista de retorno debe devolver los vectores en el mismo orden en
#  que se encontraban en L.
#  Nota: Formalmente, lo que se solicita es que retorne los puntos que pertenecen a la frontera de Pareto,
#  muy utilizada en problemas de optimización con múltiples objetivos.
#  Ejemplo: Si L=[[2,1,5],[2,2,5],[1,2,5]] en tonces pareto(L) debe retornar [[2,1,5],[1,2,5]],
#  ya que [2,2,5] es dominado por [2,1,5] pero [2,1,5] y +[1,2,5]+ no se dominan entre sí.
#  Ayuda: Se sugiere implementar una función auxiliar bool domina(vector<int> x, vector<int> y);
#  que reciba dos puntos n-dimensionales y que retorne verdadero en caso de que x domine a y.


def domina(x, y):
	for i in range(len(x)):
        #  si para todo x: x es menor que y => y domina(no queremos)
		if x[i] < y[i]: return False
	return True

def pareto(L):
    """
    Return the Pareto points from the list L.
    """
    pareto_points = []

    for x in L:
        is_pareto = True
        for y in L:
            # si 
            if x != y and domina(x, y):
                is_pareto = False
                break
        if is_pareto:
            pareto_points.append(x)

    return pareto_points

# Example usage:
L = [[2,1,5],[2,2,5],[1,2,5]]
print("For L =", L, "the Pareto points are:", pareto(L))
