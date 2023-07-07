G=  [[0, 5, 3, 0, 0],
    [0, 0, 1, 6, 4],
    [0, 1, 0, 0, 6],
    [3, 0, 0, 0, 7],
    [0, 0, 0, 2, 0]]

u=int(input("Wierzchołek startowy: "))

n=len(G)

visited=[False]*n
rodzic=[-1]*n
droga=[float("inf")]*n
droga[u]=0


while True:
    sasiedzi=[]
    for i in range(n):
        
        visited[u]=True
        j=G[u][i]
        
        
        if j!=0: 
            sasiedzi.append(i)  ##zapisywanie indeksu sąsiada wierzchołka u
            if droga[i]>(j+droga[u]): 
                droga[i]=(j+droga[u])
                rodzic[i]=u
                
                
                
            

    min=float("inf")            ## wuszikiwanie najmniejszego nieodwiedzonego indeksu
    min_indeks="null"
    for k in range(n):

        if visited[k]==False:
            if min>droga[k]: 
                min=droga[k]
                min_indeks=k

    if min==float("inf"): break

    u=int(min_indeks)



print(f"Droga {droga}\t")
print(f"Rodzice {rodzic}\t")
print(f"visited {visited}")
    
    


    

    



