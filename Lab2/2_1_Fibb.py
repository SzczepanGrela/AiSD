
    
def fibonaccii(n,tab=[0,1]):   #tablica z wartością domyślną pierwszych 2ch wyrazów
    range=len(tab)             #zmienna range określa zakres dotąd obliczonych już wyrazów (oraz stanowi funkcję licznika iteracji)
    while(range<=n):            #pętla zakończy się gdy zakres będzie większy od szukanego elemntu. tj  w tablic będzie przykładowo 5 elementów (0,1,1,2,3) by znaleźć 4ty elementy (3)// przy założeniu że pierwszym elementem jest element 0rowy 
        tab.append(tab[range-1]+tab[range-2])
        range+=1
        
    return tab[range-1]



    


n=56
print(fibonaccii(n))