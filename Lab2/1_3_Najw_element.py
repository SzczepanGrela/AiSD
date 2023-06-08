def najw(l,r,A):
    m=(r-l)+1       #zamiast funkcji len, obliczam długość fragmentu 
    if m==1: return A[l]    #gdy fragment ma jeden element, największą jego wartością jest jego jedyny element
    elif m==2: 
        if A[l]>A[r]: return A[l]   #w przypadku 2 elementów wystarczy wybrać ten większy
        else: return A[r]  
    else:  
        a=najw(l,r-(m//2),A)     #w każdym innym przypadku fragmenty dzielimy na 2 częsci (w przypadku nieparzystych liczb pierwszy fragment będzie większy) i dla nich obliczamy ich największe wartości
        b=najw(r-(m//2)+1,r,A)      #Pierwsza grupa ma ineksy od l do r-(m//2), druga grupa zaczyna się od następnego indeksu i kończy na r
        if a>b:                         #ostatnie porównanie 
            return a
        else:
            return b


tab=[101,102,103,104,4,5,6,100,8,123,2,3,4,5,6,1222]

print(najw(0,len(tab)-1,tab))             
        