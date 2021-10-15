def reversePairs(nums):
    if len(nums) < 2: return 0

    def reversePairs1(nums):
        if len(nums)==1: return 0
        if len(nums)==2: return 1 if nums[1]<nums[0] else 0
        mid = len(nums)//2
        i, count= 0,0
        while i<mid:
            j = mid
            while j<len(nums):
                if nums[i]>nums[j]:
                    count +=1
                j+=1
            i+=1
        return reversePairs1(nums[:mid])+reversePairs1(nums[mid:])+count

    return reversePairs1(nums)

nums =[1,3,2,3,1]
# nums = []
print(reversePairs(nums))

#
# count = 0
#
# def reversePairs(nums):
#     if len(nums) < 2: return 0
#
#     def mergeSort(arr):
#         if (len(arr) < 2):
#             return arr
#         middle = len(arr) // 2
#         left, right = arr[0:middle], arr[middle:]
#         return merge(mergeSort(left), mergeSort(right))
#
#     def merge(left, right):
#         result = []
#         global count
#         while left and right:
#             if left[0] <= right[0]:
#                 result.append(left.pop(0))
#             else:
#                 result.append(right.pop(0))
#                 count += len(left)
#         while left:
#             result.append(left.pop(0))
#         while right:
#             result.append(right.pop(0))
#         return result
#     mergeSort(nums)
#     return count
#
# nums =[4,5,6,7]
# # nums = []
# print(reversePairs(nums))