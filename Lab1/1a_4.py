import random

tab = [random.randint(0, 100) for _ in range(10)]
i = 1
min = tab[0]

while i < len(tab):
    if tab[i] < min:
        min = tab[i]
    i += 1
print(f"najmniejszą liczbą jest {min}")
