import random 
def suma(l,r,A):
    m=r-l+1
    if m==1:
        return A[l]
    else:
        return (suma(l,r-m//2,A)+suma((r-(m//2)+1),r,A))
    

tab=[random.randint(1, 100) for _ in range(25)]
print(suma(0,9,tab))
    