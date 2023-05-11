import random

tab = [random.randint(0, 100) for _ in range(10)]

for i in tab: print(i)

x=int(input("Podaj x: "))
i=0

while i<len(tab):
    if tab[i]==x:
        print("Liczba występuje w tablicy")
        quit()
    i+=1

print("Liczba nie występuje w tablicy")
