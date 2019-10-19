# KMP Algorithm for string matching
# complexity is O(n+m)
# n = len(string1) and m = len(string2)
def BuildPrefixTable(s1):
    m=len(s1)
    A=[0 for i in range(m)]
    j,i=0,1
    while i<m:
        if s1[j]==s1[i]:
            A[i]=j+1
            i+=1
            j+=1
        elif j > 0:
            j=A[j-1]
        else:
            A[i]=0
            i+=1
    return A

def KMP(s1,s2):
    n,m=len(s1),len(s2)
    A=BuildPrefixTable(s1)
    print(A)
    i,j = 0,0
    while i<m:
        if s1[j] == s2[i]:
            if i == m-1:
                return j-i,j
            else:
                i+=1
                j+=1
        elif i>0:
            i=A[i-1]
        else:
            j+=1
            
    return -1
    
    

s1="akshay"
s2="ksh"
print(KMP(s1,s2))






















