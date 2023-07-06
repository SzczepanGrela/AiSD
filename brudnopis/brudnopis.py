def macierz_na_liste(macierz):
    n=len(macierz)
    lista=[]
    for i in range(n):
        for j in range(i+1,n):
            if macierz[i][j]!=0:
                lista.append((i,j,macierz[i][j]))

    return lista
    
    
def list_to_mat(list):
    
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

G = [[0,1,0,0,4,8,0,0],
     [1,0,2,0,0,6,6,0],
     [0,2,0,3,0,0,2,0],
     [0,0,3,0,0,0,1,4],
     [4,0,0,0,0,5,0,0],
     [8,6,0,0,5,0,1,0],
     [0,6,2,1,0,1,0,1],
     [0,0,0,4,0,0,1,0]]
     
H=macierz_na_liste(G)
I=list_to_mat(H)
print(I)
