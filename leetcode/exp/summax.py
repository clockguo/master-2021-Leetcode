def summax(N):
    count,max1 = 0,0

    def addDigits(num):
        str1 = str(num)
        num1 = 0
        for i in range(len(str1)):
            num1 += int(str1[i])
        return num1

    while count< N//2:
        tem = N // 2
        tem = tem+count
        # max1 = max(addDigits(tem)+addDigits(N-tem),max1)
        if max1<addDigits(tem)+addDigits(N-tem):
            max1=addDigits(tem)+addDigits(N-tem)
            print(tem,N-tem)
        count+=1
    return max1
print(summax(220))
def sumn(N):
    str1 = str(N)
    x = len(str1)-1
    tem = 0
    for i in range(x):
        tem = tem*10+9
    print(tem)
    def addDigits(num):
        str1 = str(num)
        num1 = 0
        for i in range(len(str1)):
            num1 += int(str1[i])
        return num1
    result = addDigits(tem)+addDigits(N-tem)
    return result
print(sumn(220))




