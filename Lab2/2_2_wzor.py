def wzor(a=10,b=10):   #domyślna wartość w przypadku niewybrania zakresu
    tab=[["NaN"]]
    i=0
    while i<a:         #pętla iteruje się do osiągnięcia rzędu szukanej wartości
        j=0
        while j<b:      #pętla iteruje się do osiągnięcia kolumny szukanej wartości
            
            if i>0 and j==0:         
                tab[i].append(0)
            elif i==0 and j>0: 
                tab[i].append(1)
            elif i>0 and j>0: 
                k=(tab[i-1][j]+tab[i][j-1])/2
                tab[i].append(k)   
            j+=1
        i+=1
        tab.append([])   #zwiększenie tablicy o kolejną tablicę
        
    print(tab[a-1][b-1])

wzor()