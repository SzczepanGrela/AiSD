tab = []


n = int(input("Podaj ilosc elementów: "))

for i in range(n): 
    tab.append(str(input(f"podaj {i+1} element: ")))


for i in range(len(tab) - 1):
    min = i
    for j in range(i + 1, len(tab)):
        if tab[j] < tab[min]:
            min = j
    zamien = tab[i]
    tab[i] = tab[min]
    tab[min] = zamien
