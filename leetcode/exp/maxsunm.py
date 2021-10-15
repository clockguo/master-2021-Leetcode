# def maxsum(arr,n):
#     m2 = 0
#     m1 = arr[n-1]
#     for i in range(n-2,-1,-1):
#         if m2<0:
#             m2 = 0
#         tem = m1
#         m1 = max(arr[i]+m2,m1)
#         m2 = tem
#     return m1
# arr = list(map(int, input().split(',')))
# print(maxsum(arr,len(arr)))
arr = input()
arr = arr[1:-1]
arr = list(map(int, arr.split(',')))
def sort1(A):
    A.sort(key = lambda x: x % 2)
    return A
arr = sort1(arr)
print('[',end='')
for a in arr:
    if a==arr[-1]:
        print(a,end='')
        break
    print(a,end=',')
print(']')

# arr = list(map(int, input().split(',')))
# def maxProfit(prices):
#     if not prices: return 0
#     dp = [0] * len(prices)
#     for i in range(1, len(prices)):
#         if dp[i - 1] + prices[i] - prices[i - 1] > 0:
#             dp[i] = dp[i - 1] + prices[i] - prices[i - 1]
#     return max(dp)
# print(maxProfit(arr))