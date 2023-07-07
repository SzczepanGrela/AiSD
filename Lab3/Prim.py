def list_to_mat(list):          ## dla testu działania programu przy liście krawędzi na wejśćiu zamiast macierzy sąsiedztw
    
    max=list[0][0]
    for i in list:
        if i[0] > max: max=i[0]
        elif i[1]>max: max=i[1]

    mat=[[0]*(max+1) for _ in range(max+1)]
    
    for i in list:
        u=i[0] # u
        v=i[1] #v
        mat[u][v]=mat[v][u]=i[2] #w
         
        
    return mat


G = [[0,4,0,0,8,0,0,0,0],
    [4,0,8,0,11,0,0,0,0],
    [0,8,0,7,0,2,0,4,0],
    [0,0,7,0,0,0,0,14,9],
    [8,11,0,0,0,7,1,0,0],
    [0,0,2,0,7,0,6,0,0],
    [0,0,0,0,1,6,0,2,0],
    [0,0,4,14,0,0,2,0,10],
    [0,0,0,9,0,0,0,10,0]]
Q=[]
n=len(G)
visited=[False]*n
T=["null"]*(n-1)
element=0
u=0


visited[u]=True
while True:
    i=u
    for j in range(n):
        w=G[i][j]
        if w==0:  continue #iteracje bez połączeń są pomijane
        v=j
        if visited[v]==False:
            Q.append((u,v,w))


    Q=sorted(Q,key=lambda x: x[2])
    l=0
    while True:

        (u,v,w)=Q[l]
        l+=1
        if visited[v]==False:
            break

    T[element]=(u,v,w)
    element+=1
    visited[v]=True
    u=v
    del Q[l-1]
    if element==n-1: break
    
    

print(T)
    