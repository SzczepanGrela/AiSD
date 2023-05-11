def NWD_I_reku(a,b):
    
    if a==b: return print(f"NWD wynosi: {a}")
    elif a>b: return NWD_I_reku(a-b,b)
    else: return NWD_I_reku(a,b-a)


a=int(input("Podaj a: "))
b=int(input("podaj b: "))

NWD_I_reku(a,b)