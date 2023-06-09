import random
def Merge(l,m,r,A,B):
  
    i=l
    j=m
    k=l

    while i<m and j<=r:
        
        if A[i]<A[j]:
            B[k]=A[i]
            i+=1
        else: 
            B[k]=A[j]
            j+=1
        k+=1
   
    while i<m:
        B[k]=A[i]
        k+=1
        i+=1

    while j<=r:
        B[k]=A[j]
        k+=1
        j+=1

    
    for i in range(len(B)):
        if B[i]!=None:
            A[i]=B[i]
            



def MergeSort(l,r,A,B):
    if(r-l<1): return
    m=(l+r+1)//2
    MergeSort(l,m-1,A,B)
    MergeSort(m,r,A,B)
    
    Merge(l,m,r,A,B)
    
    

A = [random.randint(1, 100) for _ in range(25)]
B=[None]*len(A)
MergeSort(0,len(A)-1,A,B)
print(B)

