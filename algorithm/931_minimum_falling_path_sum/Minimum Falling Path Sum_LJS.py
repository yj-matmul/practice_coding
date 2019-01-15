def minFallingPathSum(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """
    temp = [[100 for _ in range(len(A[0]))] for __ in range(len(A))]
    temp[0] = A[0]

    for x in range(1,len(temp)):
        for i in range(len(temp[0])):
            if i==0:
                for j in range(i,2):
                    temp[x][j] = min(temp[x][j], temp[x-1][i]+A[x][j])

            elif 0<i<len(temp[0])-1:
                for j in range(i-1,i+2):
                    temp[x][j] = min(temp[x][j], temp[x - 1][i] + A[x][j])

            elif i == len(temp[0])-1:
                for j in range(i-1,i+1):
                    temp[x][j] = min(temp[x][j], temp[x - 1][i] + A[x][j])
    print(temp)

    return min(temp[-1])

print(minFallingPathSum([[1,4,7,-1],[2,3,5,6],[-10,-5,-4,1]]))

# x= [[1,4,7,-1],[2,3,5,6],[-10,-5,-4,1]]
# print(x)
# print(len(x[0]))