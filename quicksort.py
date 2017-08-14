y=0

def quicksort(A,p,r):
   if p < r:
      q=partition(A,p,r)
      quicksort(A,p,q-1)
      quicksort(A,q+1,r)

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


A=[3,6,2,8,4,9,6,8,1,4,6,5,7,8,9,1,2,3,2,8]
quicksort(A,0,len(A)-1)
print(A)
print("x=",y)
