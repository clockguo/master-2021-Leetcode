def isStraight(nums):
    i, k= 0,0
    nums = sorted(nums)
    while i<4:
        if nums[i] == 0:
            k = k+1
            i +=1
            continue
        if nums[i]+1 == nums[i+1]:
            i +=1
        else:
            if nums[i] == nums[i+1]: return False
            if nums[i]+2==nums[i+1]:
                k -=1
            elif nums[i]+3==nums[i+1]:
                k -=2
            else: return False
            if k<0: return False
            i +=1
    return  True
nums = [13,13,9,12,10]
print( isStraight(nums))

