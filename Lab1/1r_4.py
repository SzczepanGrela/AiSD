
def dzies_na_dwojk(num):
    if num == 0:
        return 0
    else:
        nieparzyste = num % 2
        return dzies_na_dwojk(num // 2) * 10 + nieparzyste



a=int(input("Podaj a: "))
a=dzies_na_dwojk(a)
print(a)