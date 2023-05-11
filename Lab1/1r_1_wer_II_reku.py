def NWD_II_reku(a,b):
    
    if b==0: return print(f"NWD wynosi: {a}")
    else: return NWD_II_reku(b,a%b)
         
a=int(input("Podaj a: "))
b=int(input("Podaj b: "))

NWD_II_reku(a,b)
