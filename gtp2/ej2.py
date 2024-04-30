# Varios: Utilizando las operaciones de la clase stack definida en el ejercicio 1, implementar 
# procedimientos que realicen cada una de las actividades siguientes
from ej1 import Stack

def ej_b(s,i):
    s2 = Stack()
    #vuelva 2 elementos de s en s2
    s2.push(s.pop())
    s2.push(s.pop())
    #elimina el elemento a reemplazar
    s.pop()
    #introduce el valor nuevo
    s.push(i)
    #vuelca s2 en s
    s.push(s2.pop())
    s.push(s2.pop())
    
def ej_c(s,n,i):
    s2 = Stack()
    
    for j in range(min(n,len(s))):
        s2.push(s.pop())
        
    s.push(i)
    s2.pop()
    while len(s2) > 0:
        s.push(s2.pop())
        
def ej_dye(s,n,i):
    s2 = Stack()
    
    for j in range(min(n,len(s))):
        s2.push(s.pop())
        
    s.push(i)
    s2.pop()
    while len(s2) > 0:
        s.push(s2.pop())