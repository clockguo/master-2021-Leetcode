def myPow(x,n):
    if n>=0:
        return x**n
    else:
        return 1/(x**(-n))

def myPow1(x,n):
    if x==0:
        return 0
    res=1
    if n<0:
        x,n=1/x,-n
    while n:
        if n&1:#是偶数返回0，不是返回1
            res *= x
        x *=x
        n>>1

print(myPow(2.1,-10))