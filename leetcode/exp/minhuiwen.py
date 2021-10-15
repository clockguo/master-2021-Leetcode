def minPalin(nums,list1):
    def longestPalindrome(s):
        if not s: return 0
        if len(s) == 1: return 1

        def childstr(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
            return j - i + 1, i + 1, j

        maxl = 1
        ans = []
        for i in range(len(s)):
            oddcount, oddl, oddr = childstr(s, i, i)
            evevcount, evel, ever = childstr(s, i, i + 1)

            if oddcount > evevcount:
                cur_l, cur_r = oddl, oddr
            else:
                cur_l, cur_r = evel, ever
            cur_maxl = max(oddcount, evevcount)
            if cur_maxl > maxl:
                maxl = cur_maxl
                ans = [cur_l, cur_r]
                # print(ans[0]+1)
        return 1 + longestPalindrome(s[:ans[0]]) + longestPalindrome(s[ans[1]:])
    ans = []
    for i in range(len(list1)):
        print(nums[list1[i][0]:list1[i][1]+1])
        ans.append(longestPalindrome(nums[list1[i][0]:list1[i][1]+1]))
    return ans
nums = 'ababaa'
list1 = [[1,4],[1,2],[0,4],[1,2]]
print(minPalin(nums,list1))


##错误的
# def longestPalindrome(s):
#     if len(s) == 1: return 1
#
#     def childstr(s, i, j):
#         while i >= 0 and j < len(s) and s[i] == s[j]:
#             i, j = i - 1, j + 1
#         return j - i - 1, i + 1, j-1
#
#     maxl = 1
#     for i in range(len(s)):
#         oddcount, oddleft, oddright = childstr(s, i, i)
#         evevcount, eveleft, everight = childstr(s, i, i + 1)
#         cur_maxl = max(oddcount, evevcount)
#         if oddcount > evevcount:
#             cur_left, cur_right = oddleft, oddright
#         else:
#             cur_left, cur_right = eveleft, everight
#         print(cur_left, cur_right)
#         if cur_maxl > maxl:
#             maxl = cur_maxl
#             maxleft = cur_left
#             maxright = cur_right
#     print(' 00---',maxleft,maxright)
#     right,left = 0,0
#     if maxright <len(s)-1:
#         right = longestPalindrome(s[maxright:])
#         print(right)
#     if maxleft>0:
#         left = longestPalindrome(s[:maxleft])
#     return right+left+1
#     # return 1 + longestPalindrome(s[:maxleft]) + longestPalindrome(s[maxright:])
# nums1 = 'qetyf'
# print('ans',longestPalindrome(nums1))