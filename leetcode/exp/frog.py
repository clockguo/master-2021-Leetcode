n = int(input())
if n==0:
    print(0)
else:
    dp0 = [0]*(n+1)
    dp1 = [0]*(n+1)
    dp1[0],dp1[1],dp0[0],dp0[1] =0,0,1,1

    for i in range(2,n+1):
        dp1[i] = dp0[i-2]
        dp0[i] = dp0[i-1]+dp1[i-1]
    print(dp1[-1]+dp0[-1])

