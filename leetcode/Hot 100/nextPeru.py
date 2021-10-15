def nextPermutation (nums):
    left, right = 0,0
    i = 0
    while i < len(nums):
        if i+1< len(nums) :
            if nums[i]<nums[i+1]:
                left,right = i, i +1
            else:
                if nums[left] <nums[i+1]:
                    right = i+1
        i +=1
    if right == 0:
        for i in range(len(nums)//2):
            nums[i],nums[-i-1] = nums[-i-1],nums[i]
        return nums
    else:
        nums[left],nums[right] = nums[right],nums[left]
        tem = nums[left+1:]
        tem = sorted(tem)
        print(tem)
        nums = nums[:left+1]+tem
        return nums
nums = [1,3,2]
print(nextPermutation(nums))


