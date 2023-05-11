"""Funkcja pomocnicza zwracająca rozwinięcie dziesiętne liczby jako łańcuch znaków."""


def int_to_str(a):
    return str(a)


tab = []


n = int(input("Podaj ilosc elementów: "))

for i in range(n):
    tab.append(int(input(f"podaj {i+1} element: ")))


for i in range(len(tab) - 1):
    min = i
    for j in range(i + 1, len(tab)):
        if int_to_str(tab[j]) < int_to_str(tab[min]):
            min = j
    zamien = tab[i]   """Zamiana elementów"""
    tab[i] = tab[min]
    tab[min] = zamien
