def exchange(nums):
    i,j = 0,len(nums)-1
    while j>i:
        if nums[i]%2:
            i +=1
            continue
        else:
            tem = nums[i]
            if not nums[j]%2:
                j -=1
                continue
            else:
                nums[i]=nums[j]
                nums[j] = tem
                i,j= i+1,j-1
    return nums

nums=[1,2,3,4,0]

print(exchange(nums))