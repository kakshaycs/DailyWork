def countingsort(A):
   k=max(A)+1
   B=[0]*len(A)
   c=[0]*k
   for i in range(len(A)):
      c[A[i]]+=1
   for i in range(1,k):
      c[i]+=c[i-1]
   for i in range(len(A)-1,-1,-1):
      B[c[A[i]]-1]=A[i]
      c[A[i]]-=1
   return B

A=[1,4,2,5,4,6,7,8,2,3,4,9,8,7,6,7,8,9]

A=countingsort(A)
print(A)
      
