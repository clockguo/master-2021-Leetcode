def cuttingRope(n):
    if n<=1:
        return False
    if n==2:
        return 1
    if n==3:
        return 2
    if n==4:
        return 4
    if n>=5:
        if n%3==1:
            return (3**(n//3-1))*4
        if n%3==2:
            return (3**(n//3))*2
        else:
            return 3 ** (n // 3)

print(cuttingRope(12))