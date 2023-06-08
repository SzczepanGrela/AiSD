def suma(l,r,A):
    m=r-l+1
    if m==1:
        return A[l]
    else:
        return (suma(l,r-m//2,A)+suma((r-(m//2)+1),r,A))
    

tab=[0,1,2,11,4,5,6,7,4,10]
print(suma(0,9,tab))
    