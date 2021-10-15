def spiralOrder(matrix):
    m, n = len(matrix), len(matrix[0])
    b, t = 0, 0
    i, j = 0, 0
    # if not m or n：return None
    ans = []
    while True:
        for j in range(b,n): ans.append(matrix[i][j])
        t +=1
        if t>m-1:break
        for i in range(t,m): ans.append(matrix[i][j])
        n -=1
        if b>n-1:break
        for j in range(n-1,b-1,-1):ans.append(matrix[i][j])
        m -=1
        if t>m-1:break
        for i in range(m-1,t-1,-1):ans.append(matrix[i][j])
        b +=1
        if b>n-1 :break
    return ans

a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
a= [[1],[2],[3]]
print(spiralOrder(a))