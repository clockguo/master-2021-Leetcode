# import math
# def cross_entropy(p, q):
#     # write code here
#     Hsum = 0
#     for i in range(len(p)):
#         # Hsum -= p[i]*math.log(q[i],10) +(1-p[i])*math.log(1-q[i],10)
#         Hsum
#     return Hsum
# print(cross_entropy([0,0.5,0.5],[0.2,0.2,0.6]))
# print(math.log(10,10))

#
# import math
# def cross_entropy(p, q):
#     # write code here
#     Hsum = 0
#     for i in range(len(p)):
#         Hsum -= p[i]*math.log(q[i],10)
#         # Hsum
#     return Hsum
# print(cross_entropy([0,0.5,0.5],[0.2,0.2,0.6]))
# print(math.log(10,10))


# def count(actions):
#     # write code here
#     set1 = {}
#     ans = []
#     for i in actions:
#         if i[0] == 'I':
#             if i[2:] in set1:
#                 set1[i[2:]] += 1
#             else:
#                 set1[i[2:]] = 1
#         elif i[0] == 'Q':
#             if i[2:] in set1:
#                 ans.append(set1[i[2:]])
#             else:
#                 ans.append(0)
#     print(ans)
#     return ans
# print(count(["I abc", "Q abc", "Q ab", "I ab", "Q ab"]))
def slove(n,str1):
    Next = [-1]*(n+1)
    left,right = 0,-1
    while left < n:
        if right == -1 or str1[left] == str1[right]:
            left,right = left+1,right+1
            Next[left] = right
        else: right = Next[right]
    if n % (n-Next[n])==0 :
        print(str1[:(n-Next[n])])
    else:
        print(str1)

str1 = input()
n = len(str1)
slove(n,str1)

