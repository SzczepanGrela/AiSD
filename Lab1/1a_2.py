
n=-1
ile=0
while n<=0:
    n=int(input("podaj n: "))

while n>0:
    a=int(input("Podaj liczbe: "))
    if a<0: ile+=1
    n-=1

print(f"W podanym ciągu występuje {ile} liczb ujemnych")



