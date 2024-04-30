#Dada una pila de nœmeros S, implementar la funci—n pancakesort(S) la cual ordena la pila solo haciendo operaciones en las cuales se invierte un rango contiguo de elementos en el tope de la pila.


import qu as qu
import stack as st

#
def invert_top_n_layers(s,n):
    q = qu.queue()    
    for i in range(n):
        q.push(s.pop()*-1)    
    while q:
        s.push(q.pop())


def get_abs_max_in_top_n_layers(s,n):    
    s2 = st.stack()
    tmp_max = abs(s.top())
    max_idx = 0    
    for idx in range(n):                
        if tmp_max < abs(s.top()):
            tmp_max = abs(s.top())
            max_idx = idx        
        s2.push(s.pop())        
    while s2:
        s.push(s2.pop())        
    return tmp_max, max_idx
    

def burntPancakeSort(s): 
    burntPancakeSortPartial(s,0)

def burntPancakeSortPartial(s,i):                         
    if i < len(s):        
        max_temp,max_idx = get_abs_max_in_top_n_layers(s,len(s)-i)        
        invert_top_n_layers(s, max_idx+1)           
        if s.top() > 0:
           invert_top_n_layers(s, 1)                   
        invert_top_n_layers(s, len(s)-i)        
        burntPancakeSortPartial(s,i+1)        
    
if __name__ == "__main__":
    s = st.stack()
    s.push(-1)
    s.push(-3)
    s.push(2)
    s.push(4)
            
    #invert_stack(s)
    print(s)
    burntPancakeSort(s)    
    print(s)