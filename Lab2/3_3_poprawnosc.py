
##### Ze względu na luźną interpretację polecenia, wybrałem algorytm sprawdzający poprawność Wielkich liter 
##### Wielkie litery w tekście będa dozowlone jedynie na początku słowa. 
##### Ponadto w słowach nie będą mogły występować cyfry ani znaki specjalne
##### Znaki specjalne mogą jedynie kończyć słowa

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
    

def czylitera(a):
    if ord(a)>=65 and ord(a)<=90: return "WL"   ## wielka litera
    elif ord(a)>=97 and ord(a)<122: return "ML" ## mała litera
    elif ord(a)>=48 and ord(a)<=57: return "C"  ##cyfra
    elif a==' ': return "Space"
    else: return "NL"  ## nie jest to litera



def poprawnosc(tekst):
    slowo=stack()
    b="W zdanie występuje błąd"
    popr="Zdanie poprawne"

    for i in tekst:
        if not slowo.isEmpty(): p=k   ## p przechowuje informacje o typie poprzedniego znaku
        k=czylitera(i)
        

        if k=='Space': slowo=stack()   ### Resetowanie stosu przy odstępach w zdaniu
        
        elif k=='ML':  
              
            if  slowo.isEmpty() or p!='C' and p!='NL':  ### mała litera może występować tylko po innych literach lub na poczatku slowa
                slowo.push(i)                                      
                
            else: return b

        elif k=='WL':                  ### Wielkie litery jedynie na początku zdania
            if slowo.isEmpty(): slowo.push(i)
            else: return b
        
        elif k=='C': 
            if slowo.isEmpty() or czylitera(slowo.peek())=='C':     ##cyfry dopuszczone jedynie z cyframi
                slowo.push(i)
            else: return b

        elif k=='NL':           #Znaki mogą występować tylko na końcu poszczególnych słów
            slowo.push(i)
            
        else: return b

    return popr


a='Ala ma kota'  # poprawne
b='Al@ m@ k0ta'  # Błąd przez 0 w środku słowa kota
c='alA ma kota'  # Błąd przez duże A 
d='Ala ma 231 kotow!!!'  #zdanie poprawne
e='A!a &ma kota' #Błąd przez znaki specjalne w innnym miejscu niż koniec słowa
tab=[a,b,c,d,e]

for j in tab:
    print(poprawnosc(j))