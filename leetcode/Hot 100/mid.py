def mid(nums1,nums2):
    def getK(k):
        left, right = 0, 0
        while True:
            if left == m:
                return nums2[right + k - 1]
            if right == n:
                return nums1[left + k - 1]
            if k == 1:
                return min(nums1[left], nums2[right])

            newid1 = min(m - 1, left + k // 2 - 1)
            newid2 = min(n - 1, right + k // 2 - 1)

            if nums1[newid1] <= nums2[newid2]:
                k -= newid1 - left + 1
                left = newid1 + 1
            else:
                k -= newid2 - right + 1
                right = newid2 +1

    m, n = len(nums1), len(nums2)
    totalL = m + n
    if totalL % 2 == 0:
        return (getK(totalL // 2) + getK(totalL // 2 + 1)) / 2.0
    else:
        return getK((totalL + 1) // 2)

nu1 = [1,2]
nu2 = [3,4]
print(mid(nu1,nu2))