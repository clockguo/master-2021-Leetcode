def binsearch(arr,target):
    left,right = 0,len(arr)-1
    while left<right:
        mid = (left+right)//2
        if target == arr[mid]:
            return arr
        elif arr[mid]<target:
            left = mid+1
        else:
            right = mid
    arr[left] = target
    return arr
print(binsearch([2,4],3))
'''
使用二分查找的方式 去找到一个最小的值排序的最长上升序列
'''
def lengthLIS(arr):
    tem = []
    if len(arr)==0: return 0
    tem.append(arr[0])
    for i in arr[1:]:
        if i > tem[-1]:
            tem.append(i)
        elif i<= tem[0]:
            tem[0] = i
        else:
            binsearch(tem,i)
    return len(tem)
print(lengthLIS([3,5,6,2,5,4,19,5,6,7,12]))

