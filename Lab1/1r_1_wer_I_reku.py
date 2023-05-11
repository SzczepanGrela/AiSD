def NWD_I_reku(a,b):
    
    if a==b: return a
    elif a>b: return NWD_I_reku(a-b,b)
    else: return NWD_I_reku(a,b-a)


a=int(input("Podaj a: "))
b=int(input("podaj b: "))

print(f"NWD wynosi: {NWD_I_reku(a,b)}")