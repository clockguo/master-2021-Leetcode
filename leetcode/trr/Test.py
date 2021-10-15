# class Solution:
#     def findAnagrams(self, s: str, p: str) :
#         left,right = 0,0
#         count  = 0
#         ans = []
#         dic,dicp = {},{}
#         for i in p:
#             if i not in dic:
#                 dic[i] = 1
#             else: dic[i] +=1
#         while right<len(s):
#             if s[right] not in dicp:
#                 dicp[s[right]] = 1
#             else: dicp[s[right]]+=1
#             if s[right] in p and dicp[s[right]] <= dic[s[right]]:
#                 count+=1
#             right +=1
#             if right-left == len(p):
#                 if count ==len(p):
#                     ans.append(left)
#                 dicp[s[left]] -=1
#                 if s[left] in p and dicp[s[left]] < dic[s[left]]: count -=1
#                 left +=1
#         return ans
#
# de = Solution()
# s= "cbaebabacd"
# p = 'abc'
# print(de.findAnagrams(s,p))

# def maxlen():
#     n = int(input())
#     k = int(input())
#     # s =""
#     # for _ in range(n):
#     #     s +=input()
#     s=input()
#     res,maxCnt,left = 0,0,0
#     dic = {}
#     i = 0
#     while i<n:
#         if s[i] not in dic:
#             dic[s[i]] = 0
#         dic[s[i]] +=1
#         maxCnt = max(maxCnt,dic[s[i]])
#         while i-left+1-maxCnt>k:
#             dic[s[left]] -=1
#             left +=1
#         res = max(res,i-left+1)
#         i +=1
#     return res
# s='aabaabaa'
# print(maxlen())
#
# def dmino(n,nums):
#     nums1 = sorted(nums,k=lambda x:x[0])
#
# def hchange():
#     m = int(input())
#     nums = []
#     ans = []
#     for i in range(m):
#         line=list(map(int,input().split()))
#         nums.append(line)
#
#     for left in range(len(nums)):
#         if nums[left][0] == 1:
#             ans.insert(nums[left][1],nums[left][2])
#         elif nums[left][0] ==2:
#             ans.pop(nums[left][1])
#         else:
#             print(ans)
# hchange()

# m = int(input())
# nums = []
# ans = []
# for i in range(m):
#     line = list(map(int, input().split()))
#     nums.append(line)
# for left in range(len(nums)):
#     if nums[left][0] == 1:
#         ans.insert(nums[left][1], nums[left][2])
#     elif nums[left][0] == 2:
#         ans.pop(nums[left][1])
#     else:
#         for i in ans:
#             print(i,end=' ')

def triange(): # 第一种是从上对下来的，书写和思路度比较的复杂，不如第二种 从低向上的方便
    m = int(input())
    nums = []
    ans = []
    for i in range(m):
        line = list(map(int, input().split()))
        nums.append(line)
    dp = []
    for i in range(m):
        tem = [0] * (2 * i + 1)
        dp.append(tem)
    print(dp)

    dp[0][0] = nums[0][0]
    for left in range(1, len(nums)):
        for right in range(len(nums[left])):
            if right == 0:
                dp[left][right] = dp[left - 1][right] + nums[left][right]
            elif right == 2 * left:
                dp[left][right] = dp[left - 1][-1] + nums[left][right]
            elif right == 1:
                if left == 1:
                    dp[left][right] = dp[0][0] + nums[left][right]
                else:
                    dp[left][right] = max(dp[left - 1][0], dp[left - 1][1]) + nums[left][right]
            elif right == 2 * left - 1 and left > 1:
                dp[left][right] = max(dp[left - 1][-1], dp[left-1][-2]) + nums[left][right]
            else:
                dp[left][right] = nums[left][right] + max(dp[left - 1][right], dp[left - 1][right - 1],
                                                          dp[left - 1][right - 2])
    max1 = max(dp[-1])
    print(dp)
    print(max1)

def triangmax(): # 最大的三角形的最大和 值
    m = int(input())
    nums = []
    dp = []
    for i in range(m):
        line = list(map(int, input().split()))
        nums.append(line)
        tem = [0] * (2 * i + 1)
        dp.append(tem)

    for i in range(len(nums[-1])):
        dp[-1][i] = nums[-1][i]
    # print(dp)
    for left in range(len(nums)-2,-1,-1):
        # print(left)
        for right in range(len(nums[left])):
            dp[left][right] = nums[left][right] + max(dp[left + 1][right], dp[left + 1][right + 1],dp[left + 1][right + 2])

    # print(dp[0][0])
    print(dp)
# triange()
# triangmax()
'''
测试数据
4
3
5 9 4
5 2 1 3 9
3 7 2 8 4 2 6
'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def buildTree(self,preorder,inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderindex = 0
        for i in range(1,len(preorder)):
            temp = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderindex]:
                node.left = TreeNode(temp)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderindex]:
                    node = stack.pop()
                    inorderindex +=1
                node.right = TreeNode(temp)
                stack.append(node.right)
        return root

    def printTree(self,root):

        if not root:
            return
        print(root.val)
        self.printTree(root.left)
        self.printTree(root.right)

pre = [3,9,20,15,7]
ino = [9,3,15,20,7]
re = Solution()
root = re.buildTree(pre,ino)
print(root.val)
re.printTree(root)

