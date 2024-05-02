# void sign_split(list<int> &L,vector< list<int> > &VL); que dada una lista L, retornar el un
# vector de listas VL las sublistas contiguas del mismo signo (el caso 0 es considerado junto con los
# positivos, es decir separa negativos de no-negativos).
#  Ejemplos:
#  		L:[4,-3,-5,-4,-5,-1,4,-1,-5,-5,1,-5,3,3,0,2,2],
#  		=> VL:[[4],[-3,-5,-4,-5,-1],[4],[-1,-5,-5],[1],[-5],[3,3,0,2,2]],
 		
# 		L:[0,4,-2,4,1,-1,-4,-4,-3,-1,-4,4,1],
#  		=> VL:[[0,4],[-2],[4,1],[-1,-4,-4,-3,-1,-4],[4,1]],
 		
# 		L:[2,-1,3,-3,3,-3,0,-1,-2,0],
#  		=> VL:[[2],[-1],[3],[-3],[3],[-3],[0],[-1,-2],[0]],

def sign_split(L, VL):
    pos = []
    neg = []
    prev = 0
    
    while L:
        # Es mas grande q 0?
        if L[0] >= 0:
            # pushea el primer elemento ahi
            pos.append(L.pop(0))
            # si el anterior era negativo
            if prev == -1:
                # pushealo a los negativos
                VL.append(neg)
                # reestablece el array
                neg = []
            # setea el actual a 1
            prev = 1  
        else:
            # es menor q 0, setea los menores a 0
            neg.append(L.pop(0))
            # si el anterior es mayor a 1
            if prev == 1:
                # hacele append a los positivos
                VL.append(pos)
                # resetea los positivos
                pos = []
            # actualiza el actual
            prev = -1
        # guarda la suma de ambos
        final = pos + neg
    VL.append(final)
    return VL

# Ejemplos de uso
L1 = [4,-3,-5,-4,-5,-1,4,-1,-5,-5,1,-5,3,3,0,2,2]
VL1 = []
sign_split(L1, VL1)

L2 = [0,4,-2,4,1,-1,-4,-4,-3,-1,-4,4,1]
VL2 = []
sign_split(L2, VL2)

L3 = [2,-1,3,-3,3,-3,0,-1,-2,0]
VL3 = []
sign_split(L3, VL3)

print("L1:", L1)
print("=> VL1:", VL1)
print("L2:", L2)
print("=> VL2:", VL2)
print("L3:", L3)
print("=> VL3:", VL3)