def merge(A,p,q,r):
   n1=q-p+1
   n2=r-q
   L=[0]*(n1+1)
   R=[0]*(n2+1)
   for i in range(0,n1):
      L[i]=A[p+i]
   for i in range(0,n2):
      R[i]=A[q+i+1]
   L[n1]=99999
   R[n2]=99999
   i=0
   j=0
   for k in range(p,r+1):
      if L[i] <= R[j]:
         A[k]=L[i]
         i+=1
      else:
         A[k]=R[j]
         j+=1


   
def merge_sort(A,p,r):
   if p<r:
      q=(p+r)//2
      merge_sort(A,p,q)
      merge_sort(A,q+1,r)
      merge(A,p,q,r)


A=[1,5,2,3,6,4,8,7,9,10]
merge_sort(A,0,9)
print(A)
