def eatmin(N,M,T,maxtrix):
    a = maxtrix[:N]
    b = maxtrix[N:]
    a1 = sorted(a,key=lambda x :-x[1])
    b1 = sorted(b,key= lambda x: -x[1])
    if a1[0][1] + b1[0][1] <T: return -1
    minc = float('inf')
    for i in range(N):
        for j in range(M):
            if a1[i][1]>=T or b1[j][1] >=T:
                if a1[i][1]>=T:
                    minc = min(minc,a1[i][0])
                if b1[i][1]>=T:
                    minc = min(minc, b1[i][0])
            elif a1[i][1]+b1[j][1] >=T:
                minc = min(minc,a1[i][0]+b1[j][0])
            else:break
    return minc
N = 5
M =1
T = 9
maxtrix = [[9,1],[4,9],[3,1],[2,3],[6,5],[9,8]]
print(eatmin(N,M,T,maxtrix))




