from collections import deque

#adiciona os pais e o filho se já não estiverem adicionados
def Add(a,p1,p2,f):
    try:
        a[f][0] = [p1,p2]
    except:
        a[f] = [[p1,p2],[]]
    try:
        a[p2][1].append(f)
    except:
        a[p2] = [[], [f]]
    try:
        a[p1][1].append(f)
    except:
        a[p1] = [[], [f]]
    return a


#percorre todo o grafo com um metodo de busca em largura  
def Busca(a,r1,r2):
    fila = deque()
    fila.append(r1)
    #a lista visitados representa os parentes do individuo 1
    visitados = [r1]

    while fila:
        u = fila.popleft()
        try:
            if (a[u][0][0] not in visitados) and (a[u][0][1] not in visitados):
                fila.append(a[u][0][0])
                visitados.append(a[u][0][0])
                fila.append(a[u][0][1])
                visitados.append(a[u][0][1])
        except:
            pass
        for v in a[u][1]:
            if v not in visitados:
                fila.append(v)
                visitados.append(v)
    #retorna o individuo 2 esta nos visitados           
    return r2 in visitados
  
#iniciliza a arvore genealogica
a={}
#leitura dos dados
N,C,T = input().split()
for i in range(int(C)):
    F=input().split()
    Add(a,F[0],F[1],F[2])
#verificação dos individos   
for i in range(int(T)):
    R=input().split()
    if (Busca(a,R[0],R[1])):
        print("verdadeiro")
    else:
        print("falso")
