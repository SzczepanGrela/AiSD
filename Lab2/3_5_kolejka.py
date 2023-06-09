class kolejka():
    
    def __init__(self):
        self.head=0
        self.tail=-1
        self.tab=[]

    def isEmpty(self):
        return  (len(self.tab)-self.head) <=0
        
    
    def enqueue(self,item):
        self.tab.append(item)
        self.tail+=1

    def dequeue(self):
        if not self.isEmpty():
            self.head+=1
            return self.tab.pop(self.head-1)
        else: return print("Pusta kolejka")
       
    def size(self):
        return len(self.tab)
        
    def __str__(self):
        return str(self.tab)    


    


