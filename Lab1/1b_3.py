def int_to_str(liczba):
    return str(liczba)


lista_elementow = []

ilosc_elementow = int(input("Podaj ilość elementów: "))

for i in range(ilosc_elementow):
    element = int(input(f"Podaj {i+1}. element: "))
    lista_elementow.append(element)

for i in range(len(lista_elementow) - 1):
    indeks_minimalnego = i
    for j in range(i + 1, len(lista_elementow)):
        if int_to_str(lista_elementow[j]) < int_to_str(lista_elementow[indeks_minimalnego]):
            indeks_minimalnego = j
    zamien = lista_elementow[i]
    lista_elementow[i] = lista_elementow[indeks_minimalnego]
    lista_elementow[indeks_minimalnego] = zamien

print(lista_elementow)
