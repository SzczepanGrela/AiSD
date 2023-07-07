G= [[0,1,0,0,0,0,0,0],
    [0,0,1,0,1,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,1,0,0,0,0,0,1],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,1,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,0]]

#u=int(input("Wierzchołek startowy: "))
u=0
n=len(G)

visited=[False]*n
rodzic=[-1]*n
droga1=[0]*n
droga2=[0]*n
czas=1
visited[u]=True
droga1[u]=czas
kolejka=[u]


while True:
    i=0
    while i<n:
        wiersz=G[u]

        if wiersz[i]!=0:
            if visited[i]==False:
                czas+=1
                droga1[i]=czas
                visited[i]=True
                rodzic[i]=u
                u=i
                kolejka.append(u)
                i=-1
        i+=1
    
    
    czas+=1
                
    if len(kolejka)!=0: 
            u=kolejka[-1]
            del kolejka[-1]
            
            droga2[u]=int(czas)
            continue
    
    
    
            
    allvisited=True
    nowy_poczatek=0

    for j in range(len(droga1)):
        if droga1[j]==0: 
             if allvisited: nowy_poczatek=j   ## zapisze tylko pierwszy chronologiczne indeks 
             allvisited=False
             

    if allvisited:
         break
    else: u=nowy_poczatek   # dla grafów rozłącznych

    
        

    



print(f"visited {visited}")
print(f"Rodzice {rodzic}\t")
print(f"Droga1 {droga1}\t")
print(f"Droga2 {droga2}\t")

           
