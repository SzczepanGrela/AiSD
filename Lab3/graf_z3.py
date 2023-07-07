


skierowany=input("Jaki rodzaj grafu?:\t skierowany? [t/n]")
wazony=input("Jaki rodzaj grafu?:\t ważony? [t/n]")
if wazony=='t': wazony=True
else: wazony=False
if skierowany=='t': skierowany=True
else: skierowany=False

i_w=int(input("Ile wierzcholkow ma miec graf? : "))
i_k=int(input("Ile krawędzi ma występować? : "))

macierz_sasiedztwa=[[0] * i_w for _ in range(i_w)]



for i in range(i_k):
    w=1
    u=int(input(f"Podaj wierzchołek u krawędzi nr {i+1}: "))
    v=int(input(f"Podaj wierzchołek v krawędzi nr {i+1}: "))
    if wazony: w=int(input(f"Podaj wagę krawędzi nr {i+1}: "))

    macierz_sasiedztwa[u][v]=w
    if not skierowany: macierz_sasiedztwa[v][u]=w


for i in macierz_sasiedztwa:
    print(i)




