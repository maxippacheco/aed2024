#Dada una pila de n�meros S, implementar la funci�n pancakesort(S) la cual ordena la pila solo haciendo operaciones en las cuales se invierte un rango contiguo de elementos en el tope de la pila.


from ej3 import Queue as qu
from ej1 import Stack as st

def invert_top_n_layers(s,n):
    q = qu.queue()    
    for i in range(n):
        q.push(s.pop())    
    while q:
        s.push(q.pop())


def get_max_in_top_n_layers(s,n):    
    s2 = st.stack()
    tmp_max = s.top()
    max_idx = 0    
    for idx in range(n):                
        if tmp_max < s.top():
            tmp_max = s.top()
            max_idx = idx        
        s2.push(s.pop())        
    while s2:
        s.push(s2.pop())        
    return tmp_max, max_idx
    

def pancakeSort(s): 
    pancakeSortPartial(s,0)

def pancakeSortPartial(s,i):                         
    if i < len(s):        
        max_temp,max_idx = get_max_in_top_n_layers(s,len(s)-i)        
        invert_top_n_layers(s, max_idx+1)            
        invert_top_n_layers(s, len(s)-i)        
        pancakeSortPartial(s,i+1)    
        
    
if __name__ == "__main__":
    s = st.stack()
    s.push('1')
    s.push('3')
    s.push('2')
    s.push('4')
            
    #invert_stack(s)
    pancakeSort(s)    