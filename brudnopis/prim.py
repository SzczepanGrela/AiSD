V = 8  # Liczba wierzchołków

# Reprezentacja grafu za pomocą tablicy krotek (u, v, w)
graph = [(6,7,1),(2,4,2),(7,8,2),(0,1,4),(2,8,4),(4,7,6),(2,3,7),(4,6,7),(0,6,8),(1,2,8),(3,5,9),(5,8,10),(1,6,11),(3,8,14)]

visited = [False] * V
key = [float('inf')] * V
parent = [-1] * V

key[0] = 0  # Inicjalizacja klucza początkowego dla wierzchołka 0

for _ in range(V - 1):
    # Znajdź wierzchołek o najmniejszym kluczu, który jeszcze nie został odwiedzony
    min_key = float('inf')
    min_index = -1
    for v in range(V):
        if not visited[v] and key[v] < min_key:
            min_key = key[v]
            min_index = v

    u = min_index
    visited[u] = True  # Oznacz bieżący wierzchołek jako odwiedzony

    # Zaktualizuj klucze dla nieodwiedzonych sąsiadów bieżącego wierzchołka
    for edge in graph:
        if edge[0] == u:
            v = edge[1]
            w = edge[2]
            if not visited[v] and w < key[v]:
                parent[v] = u
                key[v] = w

# Wyświetlanie rezultatu
print("Krawędź \tWaga")
for i in range(1, V):
    print(parent[i], "-", i, "\t", key[i])
