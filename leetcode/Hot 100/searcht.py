def searchtarget(nums,target):
    if not nums: return -1
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        # if nums[0] < nums[mid]:
        if target == nums[left]: return left

        if target > nums[right]:
            right = mid - 1
        else:
            left = mid + 1
        # else:
        #     if target > nums[right]:
        #         right = mid
        #     else :left = mid
    return -1

nums = [4,5,6,7,0,1,2]
target = 2
print(searchtarget(nums,target))