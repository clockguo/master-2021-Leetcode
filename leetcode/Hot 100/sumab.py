def work(n):
    sum1 = 0
    k = n
    left,right = 1,1
    while k>1:
        k = n/left
        right = n/k

        sum1 += (right - left +1)*k
        sum1 %=998244353
        left, right = right,right+1
    return sum1

n = 3
print(work(n))