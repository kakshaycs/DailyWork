def LEFT(i):
   return 2*i
def RIGHT(i):
   return 2*i+1

def max_heap(A,i,x):
   l=LEFT(i)
   r=RIGHT(i)
   if l < x and A[l] > A[i]:
      largest=l
   else:
      largest=i
   if r < x and A[r] > A[largest]:
      largest=r
   if largest != i:
      A[i],A[largest]=A[largest],A[i]
      max_heap(A,largest,x)

def build_maxheap(A):
   for i in range((len(A)-1)//2,0,-1):
      max_heap(A,i,len(A))

def heap_SORT(A):
   build_maxheap(A)
   x=len(A)
   for i in range((len(A)-1),0,-1):
      A[1],A[i]=A[i],A[1]
      x-=1
      max_heap(A,1,x)

A=[0,1,2,34,4,5,3,4,5,6,7,5,4,3,2,3,4,5,6,7,87,8,9,9,4,5,56,6,7,78]
heap_SORT(A)
print(A)
