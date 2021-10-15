def findNthDigit(n):
    n1,k1 = 1,1
    tip ,count= 1, 0
    while True:
        n1,tip = 9*k1*tip,tip *10
        k1 += 1
        count +=n1
        if count>n:
            count -= n1
            x = n-count
            x1,x2 = x//(k1-1),x%(k1-1)
            if x2 == 0:
                x1=x1-1
            for i in range(len(str(int(tip/10 + x1)))):
                if x2 == 0:
                    return int(str(int(tip/10 + x1))[-1])
                elif i == x2-1:
                    return int(str(int(tip/10 + x1))[i])
        # print(count)
print(findNthDigit(25))