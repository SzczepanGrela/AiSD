G=  [[0,1,0,0,1,0,0,0],
     [1,0,0,0,0,1,0,0],
     [0,0,0,1,0,1,1,0],
     [0,0,1,0,0,0,1,1],
     [1,0,0,0,0,0,0,0],
     [0,1,1,0,0,0,1,0],
     [0,0,1,1,0,1,0,0],
     [0,0,0,1,0,0,1,0]]

#u=int(input("Wierzchołek startowy: "))
u=3
n=len(G)

visited=[False]*n
rodzic=[-1]*n
droga=[-1]*n
droga[u]=0
kolejka=[]
while True:
    alltrue=True
    visited[u]=True
    for i in range(n):
        
        
        j=G[u][i]
        
        
        if visited[i]==False: alltrue=False
        if j!=0 and droga[i]==-1: 
                    droga[i]=(j+droga[u])
                    rodzic[i]=u
                    kolejka.append(i)
                    alltrue=False   
            
    
    if len(kolejka)!=0: 
        u=kolejka[0]
        del kolejka[0]
    if alltrue: break



print(f"Droga {droga}\t")
print(f"Rodzice {rodzic}\t")
print(f"visited {visited}")
    
    
