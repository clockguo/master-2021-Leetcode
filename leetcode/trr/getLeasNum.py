def getNum(arr,k):
    i, j = 0,len(arr)-1
    def partition(arr,left, right):
        pivot = left
        index = pivot + 1
        i = index
        while i<=right:
            if arr[i] < arr[pivot]:
                arr[i], arr[index] = arr[index], arr[i]
                index += 1
            i +=1
        arr[pivot], arr[index-1] = arr[index-1],arr[pivot]
        return index -1
    while i<j:
        kt = partition(arr, i, j)
        if kt == k:
            return arr[:kt]
        elif kt>k:
            j = kt-1
        else:
            i = kt+1

    return arr[:k]

arr = [0,0,1,2,4,2,2,3,1,4]
k = 8
print(getNum(arr,k))