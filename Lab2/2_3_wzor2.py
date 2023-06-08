def wzor(n,tab=[1,1]):
    range=len(tab)
    while range<n+1:
        tab.append(2*tab[range-1]-tab[range-2])  
        range+=1

    print(tab[n])


wzor(50)  