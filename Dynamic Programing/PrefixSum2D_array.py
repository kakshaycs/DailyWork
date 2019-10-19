# 2d prefix sum
# dynamic programing
# find sum of submatrix in O(1)

def prefixSum2d(Array, n, m):
    pSum = [[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            pSum[i][j] = pSum[i-1][j] + pSum[i][j-1] +Array[i-1][j-1] -pSum[i-1][j-1]
    return pSum

def SumofSubmatrix(psum,i,j,k,l):
    
    x=psum[k][l] +psum[i-1][j-1] - psum[k][j-1] -psum[i-1][l]
    return x


Array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n,m = 4,4
for i in range(n):
    print(*Array[i])

PrefixSum = prefixSum2d(Array,n,m)
print("PrefixSum")
for i in range(1,n+1):
    print(*PrefixSum[i][1:])

print(SumofSubmatrix(PrefixSum,2,2,3,3))
