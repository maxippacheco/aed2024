from ej3 import Queue

def ej4_a(q,i):
    q.pop()
    q.pop()
    
    q2 = Queue()
    q2.push(i)
    
    while len(q) > 0:
        q2.push(q.pop())
        
def ej4_b(q,i):
    q2 = Queue()
    
    q2.push(q.pop())
    q2.push(q.pop())
    
    q2.push(i)
    
    while len(q) > 0:
        q2.push(q.pop())
    while len(q2) > 0:
        q.push(q2.pop())
        
def ej4_c(q,i):
    q2 = Queue()
    
    for j in range(len(q)-1):
        q2.push(q.pop())
    q.pop()
    
    q2.push()
    
    while len(q2) > 0:
        q.push(q2.pop())
        
def ej4_e(q,i):
    q.push(i)