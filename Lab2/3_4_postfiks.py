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
    
def cyfr_znak_space(a):
    if ord(a) >= 48 and ord(a) <=57: return 'L'   ## Liczby znajdują się między 48 i 57 indeksem ASCII
    elif a=='*' or a=='+' or a=='-' or a=='/' or a=='^': return  'O'
   
    elif a=='=': return 'W' ##Wynik

    else: return 'blank'   ## Wszystkie znaki niebędące liczbą lub operatorem zostaną traktowane jako spacja


    

def operacja(a, b, oper):
    if oper == '+': return int(a)+int(b)
    elif oper == '-': return int(a)-int(b)
    elif oper == '*': return int(a)*int(b)
    elif oper == '/': return int(a)/int(b)
    elif oper == '^': return int(a)**int(b)

    
def postfiks(tekst):
    argumenty = stack()

    for i in range(len(tekst)):     
        k=cyfr_znak_space(tekst[i])       # w zmiennej k przechowuje się informacje o typu znaku
        if k=='O': 
            b=argumenty.pop()               
            a=argumenty.pop()
            argumenty.push(operacja(a,b,tekst[i]))     # Na stos wrzucam wynik operacji
        elif k=='L': 
        
            
            argumenty.push(tekst[i])
            
        elif k=='W':
            return print(argumenty.pop())




tekst="73+52-2^*="  ## przykłądowy tekst z zadania 

postfiks(tekst)

