def bT(cu=[]):
    if len(cu) == 3:
        ans.append(cu[:])
        return
    for i in nums:
        if i in cu:
            continue
        cu.append(i)
        bT(cu)
        cu.pop()
    return ans
nums = []
ans = []
for i in range(10):
    nums.append(chr(ord('0')+i))
for i in range(26):
    nums.append(chr(ord('a')+i))
print(bT())