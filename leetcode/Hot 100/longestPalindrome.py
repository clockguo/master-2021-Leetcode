# def longestPalindrome(s):
#     if len(s)<2: return s
#     def childstr(s,i,j):
#         while i>=0 and j<len(s) and s[i]==s[j]:
#             i,j = i-1,j+1
#         return j-i+1,s[i+1:j]
#     maxl = 1
#     ans = s[0]
#     for i in range(len(s)):
#         oddcount,oddstr = childstr(s,i,i)
#         evevcount,evevstr = childstr(s,i,i+1)
#
#         cur_max = oddstr if oddcount>evevcount else evevstr
#         cur_maxl = max(oddcount,evevcount)
#         if cur_maxl >maxl:
#             maxl = cur_maxl
#             ans = cur_max
#     return  ans


s = "ababaa"
# print(longestPalindrome(s))

def longestPalindrome(s):
    if not s: return 0
    if len(s)==1: return 1
    def childstr(s,i,j):
        while i>=0 and j<len(s) and s[i]==s[j]:
            i,j = i-1,j+1
        return j-i+1,i+1,j
    maxl = 1
    ans = []
    for i in range(len(s)):
        oddcount,oddl,oddr = childstr(s,i,i)
        evevcount,evel,ever = childstr(s,i,i+1)

        if oddcount>evevcount:
            cur_l, cur_r = oddl, oddr
        else: cur_l,cur_r = evel,ever
        cur_maxl = max(oddcount,evevcount)
        if cur_maxl >maxl:
            maxl = cur_maxl
            ans = [cur_l,cur_r]
            # print(ans[0]+1)
    return  1+longestPalindrome(s[:ans[0]])+longestPalindrome(s[ans[1]:])

print(longestPalindrome(s))
