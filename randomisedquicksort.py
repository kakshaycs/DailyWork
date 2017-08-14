import random

y=0
def partition(A,p,r):
   global y
   x=A[r]
   i=p-1
   for j in range(p,r):
      y+=1
      if A[j] <= x:
         i=i+1
         A[i],A[j]=A[j],A[i]
         
   A[i+1],A[r]=A[r],A[i+1]
   return i+1

def randomPartition(A,p,r):
   i=random.randint(p,r)
   A[i],A[r]=A[r],A[i]
   return partition(A,p,r)
   
def Randomquicksort(A,p,r):
   if p < r:
      
      q=randomPartition(A,p,r)
      Randomquicksort(A,p,q-1)
      Randomquicksort(A,q+1,r)


A=[3,6,2,8,4,9,6,8,1,4,6,5,7,8,9,1,2,3,2,8]
Randomquicksort(A,0,len(A)-1)
print(A)
print(y)
