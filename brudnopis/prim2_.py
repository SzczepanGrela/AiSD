Q = []
n = 8  
visited = [False] * n
T = set()
u = 0
visited[u] = True

krawedzie = [(6,7,1),(2,4,2),(7,8,2),(0,1,4),(2,8,4),(4,7,6),(2,3,7),(4,6,7),(0,6,8),(1,2,8),(3,5,9),(5,8,10),(1,6,11),(3,8,14)]
sasiedzi=[["null"]]*8
for i in krawedzie:
    
    if sasiedzi[i[0]][0]!="null":
        sasiedzi[i[0]].append((i[1],i[2]))
    else: sasiedzi[i[0]]=((i[1],i[2]))
    
    if sasiedzi[i[0]][0]!="null":
        sasiedzi[i[0]].append([i[1],i[2]])
    else: sasiedzi[i[0]]=((i[1],i[2]))
    #sasiedzi[i[1]].append((i[0],i[2]))




for i in range(1, n):
    j=0
    for j in len(sasiedzi[j]):
        if visited[v] == False:
            Q.append((u, v, w))  

    while True:
        
        (u, v, w) = Q[0]  
        Q.pop(0)  

      
        while visited[v] == True:
            T.add((u, v, w))
            visited[v] = True
            u = v

        if len(Q) == 0:
            break


print("Krawędź \tWaga")
for edge in T:
    u, v, w = edge
    print(f"{u} - {v}\t\t{w}")