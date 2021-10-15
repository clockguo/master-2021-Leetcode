# def lengthOfLongestSubstring(s: str) -> int:
#     left, right, dic = -1, 0, {}
#     for i in range(len(s)):
#         if s[i] in dic and dic[s[i]] > left:
#             left, dic[s[i]] = dic[s[i]], i
#         else:
#             dic[s[i]] = i
#             right = max(right, i - left)
#     return right
#
# s = "nnnnnbb"
# print(lengthOfLongestSubstring(s))

# paixu
# a = [[5,2,3],[4,5,6],[12,4,6]]
# print(a)
# b = sorted(a,key=lambda x:(-x[0],x[1]))
# print(b)


#
# def dmino(n,nums):
#     nums1 = sorted(nums,key=lambda x:x[0])
#     nums2 = [0]*n
#     for i in range(n):
#         nums2[i] = nums1[i][1]
#
#     po = [1] * n
#
#     for i in range(n):
#         for j in range(i + 1):
#             if nums2[i] > nums2[j]:
#                 po[i] = max(po[j] + 1, po[i])
#     return max(po)
#
# nums1 = [[5,5],[3,1],[2,6],[4,2],[1,4]]
# print(dmino(5,nums1))

#
# print(graph)
## one
# a = 5
# b = 6
# sum1 = 0
# for i in range(1,((b+1)//2)):
#     sum1 +=int(a/i)
#
# print(sum1+min((a+1)//2,(b+1)//2))

## one-2
# a = 5
# b = 6
# sum1 =0
# tem = a
# for i in range(1,b+1):
#     if tem == a//i:
#         sum1 += tem


##two
# class listnode:
#     def __init__(self,x):
#         self.x = x
#         self.next = None
# nums= [12,2,2,2,3,5]
# head = listnode(nums[0])
# right = head
# tem = nums[-1]
# count ,i= 1,0
# while i <len(nums):
#     if tem != nums[i]:
#         tem = nums[i]
#     else:
#         i +=1
#         continue
#
#     while count <2:
#         l = listnode(tem)
#         right.next = l
#         right = l
#         count +=1
#     count = 0
#     i+=1
#
# while head:
#     print(head.x)
#     head = head.next

## three
# #
# nums =[1,2,-3]
# res = 0
# ans = [[]]
# for i in nums:
#     ans += [tem + [i] for tem in ans]
# print(ans)
# for i in ans:
#     if sum(i)!=0:
#         res +=1
# print(res-1)
# # size =10
# # for i in range(int(size/2)-1,-1,-1):
# #     print(i)
#
#
# line1 = [2,3,4]
# nums = [1]
# for i in line1:
#     nums += [tem*i for tem in nums]
#
# print(nums)
def nn (num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return  factorial

def f(n, m):
    if (n < 1 or m < 1):
        return 0
    if (n == 1 and m == 1):
        return 1
    if (n <= m):
        return 1 + f(n, n - 1)
    return f(n, m - 1) + f(n - m, m)

print(f(10, 5))

# lines = list(map(int,input().split()))
# N,M = lines[0],lines[1]
#
# dp = [1]*(N+1)
# for i in range(2,N+1):
#     dp[i] = dp[i-1]+M-1
# print(dp[-1])

# def maxSlidingWindow(nums, k):
#     if k == 1: return nums
#     j, i = 1, 0
#     maxt, maxid = [nums[0]], [0]
#     ans = []
#     while j < len(nums):
#         if maxid[0] < j - k + 1:
#             maxt.pop(0)
#             maxid.pop(0)
#         if nums[j] <= maxt[-1]:
#             maxt.append(nums[j])
#             maxid.append(j)
#         else:
#             for i in maxt[::-1]:
#                 if nums[j] > i:
#                     maxt.pop()
#                     maxid.pop()
#                 else:
#                     break
#             maxt.append(nums[j])
#             maxid.append(j)
#         if j >= k - 1:
#             ans.append(maxt[0])
#         j += 1
#     return ans
#
# lines = list(map(int,input().split(',')))
# k = int(input())
# arr = maxSlidingWindow(lines,k)
# for i in range(len(arr)):
#     if i == len(arr)-1:
#         print(arr[i])
#         break
#     print(arr[i],end=',')

lines = list(map(int,input().split(',')))
lines.sort()
print(lines[len(lines)//2])