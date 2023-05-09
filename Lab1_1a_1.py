import math


a=float(input("Podaj a: "))
b=float(input("Podaj b: "))
c=float(input("Podaj c: "))

if(a!=0):
    d=b*b-4*a*c
    if d>=0:
        if d==0:
            x1=-b/(2*a)
            print(f"Pierwiastkiem jest {x1}")
        else:
            x1=(-b-math.sqrt(d))/(2*a)
            x2=(-b+math.sqrt(d))/(2*a)
            print(f"Pierwiastkami jest {x1} i {x2}")
    else:
        print("Nie występują pierwiastki w przedziale rzeczywistym")
else:
    print("To nie jest równanie kwadratowe")


    
