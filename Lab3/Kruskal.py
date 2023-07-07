
T = []
V = set()
G = [(6,7,1),(2,4,2),(7,8,2),(0,1,4),(2,8,4),(4,7,6),(2,3,7),(4,6,7),(0,6,8),(1,2,8),(3,5,9),(5,8,10),(1,6,11),(3,8,14)]

for krawedz in G:
    u, v, w = krawedz
    V.add(u)
    V.add(v)

podzbiory = [{wierzch} for wierzch in V]

#sortowanie po wadze 
G.sort(key=lambda krawedz: krawedz[2])

for krawedz in G:
    u, v, w = krawedz
    # Wyszukiwanie podzbiorów zawierających u i v
    for podzbior in podzbiory:
        if u in podzbior:
            u_set = podzbior
        if v in podzbior:
            v_set = podzbior

    # Jeśli u i v należą do różnych podzbiorów, połącz podzbiory i dodaj krawędź (u, v) do T
    if u_set != v_set:
        podzbiory.remove(u_set)
        podzbiory.remove(v_set)
        new_set = u_set.union(v_set)
        podzbiory.append(new_set)
        T.append((u, v, w))



print(T)



