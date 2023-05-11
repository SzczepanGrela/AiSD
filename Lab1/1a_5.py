import random

tab = [[random.randint(-100, 100) for _ in range(10)] for _ in range(10)]
i=0
j=1
min=tab[0][0]
n=len(tab)

while i<n:
    m=len(tab[i])
    while j<m:
        if tab[i][j]<min: min=tab[i][j]
        j+=1
    i+=1
    j=0

print(f"Najmniejszą liczbą jest {min}")
