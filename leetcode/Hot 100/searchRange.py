def searchRange(nums,target):

    def twoserch(nums,target):
        left, right = 0,len(nums)-1
        if len(nums)==1 and nums[0]==target: return 0
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>target:
                right = mid-1
            elif nums[mid]==target:
                return mid
            else:
                left = mid+1
        return -1
    mid = twoserch(nums,target)
    if mid==-1:
        return [-1,-1]
    i,j = mid-1,mid+1
    while True:
        if i>=0 and nums[i]==target:
            i -=1
        if j<len(nums) and nums[j] == target:
            j +=1
        if i<0 and j>=len(nums) or i<0 and nums[j]!=target or j>=len(nums) and nums[i]!=target or nums[i]!=target and nums[j]!=target:
            break

    return [i+1,j-1]

nums = [1,2,3]
target =3
print(searchRange(nums,target))


