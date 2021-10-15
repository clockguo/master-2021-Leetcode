def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right: #只要找到比pivot小的移动就可以了 遍历一次找到小的向前移动
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

a= [5,2,20,7,4,3]
# print(a)
# print(partition(a,0,len(a)-1),a)
# print(quickSort(a))

def Quick_sort(arr,left=None,right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition1(arr, left, right)
        Quick_sort(arr, left, partitionIndex - 1)
        Quick_sort(arr, partitionIndex + 1, right)
    return arr

def partition1(arr, left, right):
    pivot = arr[left]
    while left<right:
        while left<right and arr[right]>=pivot: right -=1
        arr[left] = arr[right]
        while left<right and arr[left]<=pivot: left +=1
        arr[right] = arr[left]
    arr[left] = pivot
    return right

print(partition1(a,0,len(a)-1),a)
print(Quick_sort(a))