def countingsort(A,exp):
   B=[0]*len(A)
   c=[0]*10
   for i in range(len(A)):
      index=A[i]//exp
      c[index%10]+=1
   for i in range(1,10):
      c[i]+=c[i-1]
   for i in range(len(A)-1,-1,-1):
      index=A[i]//exp
      B[c[index%10]-1]= A[i]
      c[index%10]-=1
   return B

def radixSort(A):
   m=max(A)
   exp=1
   while m//exp>0:
      A=countingsort(A,exp)
      exp*=10
   return A
   
A=[23,345,23,12,45,6,7,89,34,65,78,98]
A=radixSort(A)
print(A)
      

