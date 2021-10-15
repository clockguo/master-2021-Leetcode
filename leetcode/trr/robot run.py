def movingCount(m,n,k):
    def add(i, j):
        s = 0
        while i > 0 or j > 0:
            s, i = s + i % 10, i // 10
            s, j = s + j % 10, j // 10
        return s

    matrix=[[-1 for col in range(n)] for row in range(m)]

    def movenow(i,j,matrix,k):
        if not 0<=i<m or not 0<=j<n : return 0
        if add(i,j)>k: return 0
        if matrix[i][j]==0 or matrix[i][j]==1: return 0
        matrix[i][j]=0
        movenow(i-1, j ,matrix, k)
        movenow(i + 1, j, matrix, k)
        movenow(i , j-1, matrix, k)
        movenow(i , j+1, matrix, k)
        matrix[i][j]=1
        return 1
    s=0
    movenow(0,0,matrix,k)
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==1: s+=1
    print(matrix)
    return s

print(movingCount(11,8,16))