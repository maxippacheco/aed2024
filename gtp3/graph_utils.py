import graphviz as gv

def buildGraph(G):
  GG = gv.Graph(strict=True)    
  for k in G:
    for v in G[k]:
      GG.edge(str(v),str(k))
  return GG

def plotGraph(G):
  GG = buildGraph(G)
  GG.render(view=True)  

def esCamino(G,L):
  for i in range(len(L)-1):        
    print(L[(i+1)%len(L)])
    print(G[L[i%len(L)]])
    if L[(i+1)%len(L)] not in G[L[i%len(L)]]:
      return False
  return True

def plotPath(G,P):
  if esCamino(G,P):
    GG = buildGraph(G)
    for i in range(len(P)-1):
      GG.edge(str(P[i]),str(P[i+1]),_attributes={"penwidth":"2","color":"red"})
    GG.render(view=True)  