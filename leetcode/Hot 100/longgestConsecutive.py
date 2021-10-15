def longestConsecutive(nums): #hash 表法
    dic, maxl = {}, 0
    for i in nums:
        if i not in dic:
            left = dic.get(i - 1, 0)
            right = dic.get(i + 1, 0)

            nowi = left + right + 1
            if maxl < nowi:
                maxl = nowi
            dic[i], dic[i - left], dic[i + right] = nowi, nowi, nowi

    return maxl

nums = [1,2,0,1]

print(longestConsecutive(nums))
