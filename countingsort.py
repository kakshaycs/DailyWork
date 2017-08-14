def countingsort(A,B,k):
   c=[0]*k
   print(c)
   for i in range(len(A)):
      c[A[i]]+=1
   print(c)
   for i in range(1,k):
      c[i]+=c[i-1]
   print(c)
   for i in range(len(A)):
      B[c[A[i]]-1]=A[i]
      c[A[i]]-=1
   print(B)

A=[1,4,2,5,4,6,7,8,2,3,4,9,8,7,6,7,8,9]
B=[0]*len(A)
countingsort(A,B,max(A)+1)
      
