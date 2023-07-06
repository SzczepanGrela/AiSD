# Prim's Algorithm in Python


# number of vertices in graph

#creating graph by adjacency matrix method
G = [[0,1,0,0,4,0,0,0],
     [1,0,2,0,0,0,0,0],
     [0,2,0,0,0,0,2,0],
     [0,0,0,0,0,0,1,0],
     [4,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,1,0],
     [0,0,2,1,0,1,0,1],
     [0,0,0,0,0,0,1,0]]
N = len(G)
INF = 9999999
visited = [False] * N

no_edge = 0

visited[0] = True

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):
    
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if visited[m]:
            for n in range(N):
                if ((not visited[n]) and G[m][n]):  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":\t" + str(G[a][b]))
    visited[b] = True
    no_edge += 1
