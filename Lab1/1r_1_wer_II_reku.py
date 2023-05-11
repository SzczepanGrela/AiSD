def NWD_II_reku(a,b):
    
    if b==0: return a
    else: return NWD_II_reku(b,a%b)
         
a=int(input("Podaj a: "))
b=int(input("Podaj b: "))

print(f"NWD wynosi: {NWD_II_reku(a,b)}")
