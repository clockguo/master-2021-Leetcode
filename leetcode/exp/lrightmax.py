n = int(input())
arr = list(map(int, input().split()))
ansmax = 0
stack = []

leftFirstMax = [0]*n
rightFirstMax = [0]*n
for i in range(n):
    samei = []
    while len(stack)!=0 and arr[i]>=arr[stack[-1]]:
        m = stack.pop()
        if arr[i] > arr[m]:
            rightFirstMax[m] = i+1
        else:
            samei.append(m)
    if len(stack)!=0:
        leftFirstMax[i] = stack[-1]+1
    while len(samei)!=0:
        stack.append(samei.pop())
    stack.append(i)
for i in range(n):
    if leftFirstMax[i]*rightFirstMax[i]>ansmax:
        ansmax = leftFirstMax[i]*rightFirstMax[i]
# print(leftFirstMax)
# print(rightFirstMax)
print(ansmax)
# import re
# a='34'
# i = '12345621'
# a1 = re.sub(a,'',i)
# print(a1)