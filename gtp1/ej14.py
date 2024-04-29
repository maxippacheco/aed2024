# MergeSort. Programar una función mergesort(L) que reciba una lista L desordenada y la ordene
# en forma ascendente mediante la siguiente estrategia recursiva: Si la lista está vacía o tiene un sólo
# elemento ya está ordenada. Si no, se parte la lista en dos sublistas y se las ordena a cada una de forma
# recursiva. Luego se mezclan (fusionan) cada una de las sublistas ya ordenadas.

def merge(L1,L2,L):
    while L1 and L2:
        if L1[0] < L2[0]:
          L.append(L1.pop(0))
        else:
          L.append(L2.pop(0))
    while L1:
      L.append(L1.pop(0))
    while L2:
      L.append(L2.pop(0))
    return L

def merge_sort(L):
    if len(L) <= 1:
      return L
    
    mitad = len(L) // 2
    izq = L[:mitad]
    der = L[mitad:]
    
    izq_ord = merge_sort(izq)
    der_ord = merge_sort(der)

    return merge(izq_ord, der_ord, [])

L3 = [3, 4, 2, 6, 11, 3, 9]
L4 = merge_sort(L3)
print(L4)