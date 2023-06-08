class stack():
    def __init__(self):
        self.stack = list()

    def isEmpty(self):
        return len(self.stack) <=0

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty(): return None
        else: return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return None
        else: return self.stack[len(self.stack)-1]
    
    def __str__(self):
        return str(self.stack)
    




def nawiasy(tekst):
    stos= stack()
    for i in tekst:
        if i=="(" or i=="[" or i=="{": stos.push(i)
        elif i==")" or i=="]" or i=="}": 
           if stos.isEmpty(): return print("Błąd w tekście") ##Więcej zamykającyh niż otwierających
           elif ord(stos.peek()) == ord(i)-1 or ord(stos.peek()) == ord(i)-2: stos.pop()       ##Porównanie znaków na tablicy ascii 
           else: return print("Błąd w tekście")   ##zamknięcie złym nawiasem  
        
    if not stos.isEmpty(): return print("Błąd w tekście") ## Więcej otwierających niż zamykających 
    else: return print ("Tekst poprawny")


przyk_tekst=['(()()()())','(((())))','(()((())()))','((((((())','()))','(()()(()']

for i in przyk_tekst:
    nawiasy(i)




