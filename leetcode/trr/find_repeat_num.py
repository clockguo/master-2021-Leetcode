def find_repeat_number(nums):
    nums_dict={}
    print(nums_dict)
    for num in nums:
        if num in nums_dict:
            nums_dict[num] +=1
        else:
            nums_dict[num] = 1
    print(nums_dict)
    for num in nums:
        if nums_dict[num] > 1:
            return num
    return False


nums=[2, 3, 1, 0, 2, 5, 3]
print(find_repeat_number(nums))

