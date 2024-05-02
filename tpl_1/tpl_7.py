# Implemente una función void sign_join(vector< list<int> > &VL,list<int> &L); que, dado un vector de listas VL
# generar una lista L donde están primero concatenados todos la primera 
# subsecuencia de no-negativos de VL[0], VL[1], ... Después los negativos.
# Después nuevamente los no-negativos.
# Asi siguiendo hasta que se acaban todos los VL.
# Ejemplos:
#   VL: [[1,2,-1,-2,3,4,-3,-4],[5,6,-5,-6,7,8,-7,-8],[-9,-10]],
#   => L: [1,2,5,6,-1,-2,-5,-6,-9,-10,3,4,7,8,-3,-4,-7,-8],
# 	VL: [[0,4,-2,4,1],[-1,-4,-4,-3,-1],[-4,4,1,3,-2],[0,3,-2,4,-5],[-5,-5,-1,-3,-2]],
# 	=> L:[0,4,0,3,-2,-1,-4,-4,-3,-1,-4,-2,-5,-5,-1,-3,-2,4,1,4,1,3,4,-2,-5]
# 	VL:[[-1,-1,-1,3],[-5,3,1,2],[0,2,4,-3],[-3,0,4,-3]],
# 	=> L:[0,2,4,-1,-1,-1,-5,-3,-3,3,3,1,2,0,4,-3],

# todo esta mal
def sign_join(VL: list, L: list):
	is_positive = True
	for sublist in VL:
		for num in sublist:
			if num >= 0 and is_positive:
				L.append(num)
			elif num < 0 and is_positive:
				is_positive = False
				L.append(num)
			elif num >= 0 and not is_positive:
				is_positive = True
				L.append(num)
			else: L.append(num)

# Example usage
VL =  [[1,2,-1,-2,3,4,-3,-4],[5,6,-5,-6,7,8,-7,-8],[-9,-10]]
L = []

sign_join(VL, L)

print(L)
