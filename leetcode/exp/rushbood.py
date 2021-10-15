def rushb(nums):
    def over(left,right):
        if left>right: return 0
        min1 = min(nums[left:right+1])
        for i in range(left,right+1):
            nums[i] -= min1
            if nums[i]==0:
                minid = i
            print(i)
        return min(right-left+1,over(left,minid-1)+over(minid+1,right)+min1)
    return over(0,len(nums)-1)
nums = [5,1,1,2,2]
print(rushb(nums))