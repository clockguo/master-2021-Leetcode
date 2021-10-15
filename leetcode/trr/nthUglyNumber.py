def nthUglyNumber(n):
    if n <7:
        return n
    count, idx1,idx2,idx3=1,0,0,0
    nums = [0]*n
    nums[0] = 1
    while count<n:
        nums[count] = min(nums[idx1]*2,min(nums[idx2]*3,nums[idx3]*5))
        if nums[count]==nums[idx1]*2: idx1 +=1
        if nums[count] == nums[idx2] * 3: idx2 += 1
        if nums[count] == nums[idx3] * 5: idx3 += 1
        count +=1
    return nums[n-1]

print(nthUglyNumber(10))


