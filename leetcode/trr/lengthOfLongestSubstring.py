def lengthOfLongestSubstring(s):
    list1 = []
    maxv, maxv1 = 0, 0
    for i in s:
        if i not in list1:
            maxv += 1
        else:
            for j in range(len(list1)):
                if list1[j] == i:
                    list1 = list1[j + 1:]
                    maxv -= j
                    break
        list1.append(i)
        if maxv1 < maxv:
            maxv1 = maxv
    return maxv1

a = "abcabcbb"
print(lengthOfLongestSubstring(a))