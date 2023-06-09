import os

class kolejka():
    
    def __init__(self):
        
        self.tab=[]
        self.head=0
        self.tail=len(self.tab)-1

    def isEmpty(self):
        return  (len(self.tab)-self.head) <=0
        
    
    def enqueue(self,item):
        self.tab.append(item)
        self.tail+=1

    def enqueuetab(self,item):
        for i in range(len(item)):
            self.tab.append(item[i])
        self.tail=len(self.tab)-1
    
    def dequeue(self):
        if not self.isEmpty():
            self.tail-=1
            return self.tab.pop(self.head)
        else: return print("Pusta kolejka")

    def peek(self):
        if not self.isEmpty():
            return self.tab[self.head]
        else: return print("Pusta kolejka")
       
    def size(self):
        return len(self.tab)
        
    def __str__(self):
        return str(self.tab)  

def podanie(osoby):
    
   osoby.enqueue(osoby.peek())
   osoby.dequeue()

def odpadanie(osoby):
    print(f"Odpada {osoby.dequeue()}")
    

def gra_w_ziemniaka(n,imiona):  ##n- liczba przerzutów po jakiej dochodzi do eliminacji
    osoby=kolejka()
    osoby.enqueuetab(imiona)
    while(osoby.size()>1):
        

        for i in range(n):   ### po n przerzutach odpada osoba na początku tablicy
            
            podanie(osoby)
        
        odpadanie(osoby)
    
    print(f"Zwycięzcą zostaje: {osoby.peek()}")
        


imiona=['Tomek','Michal','Basia','Kasia','Małgosia','Jędrzej','Krzysiek','Monika','Wiktoria','Kuba']

gra_w_ziemniaka(152,imiona)