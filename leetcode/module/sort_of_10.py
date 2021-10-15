
# select sort :从待排序的数据元素中选出最小的一个元素，
# 存放在序列的起始位置，直到全部带排序的数据元素排完
def select_sort(lists):
    n = len(lists)
    for i in range(n):
        for j in range(i+1,n):
            if lists[i]>lists[j]:
                lists[i],lists[j] = lists[j],lists[i]
    return lists
# list1 = [2,1,6,4,7,4,5]
# print(select_sort(list1))

#insert sort 比较顺序是从后向前比较 最优是O(n) 一般 O(n)
def insert_sort(lists):
    n = len(lists)
    for i in range(1,n):
        key = lists[i]
        j = i-1
        while j>=0:
            if lists[j] >key:
                lists[j+1] = lists[j]
                lists[j] = key
            else: break #因为右后向前，所以比最后一个hai big的话，直接跳出^-^
            j -=1
    return lists

# list1 = [2,1,6,4,7,4,5]
# print(insert_sort(list1))

# shell sort 把记录按下标的一定增量进行分组，
# 对每组直接使用插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，
# 当增量减至1时，整个文件恰被分成一组，算法便终止。
def shell_sort(lists):
    n = len(lists)
    dist = n//2
    while dist>0:
        for i in range(dist,n):
            temp = lists[i]
            j = i
            while j>=dist and temp <lists[j-dist]:
                lists[j] = lists[j-dist]
                j -=dist
            lists[j] = temp
        dist //=2
    return lists

# list1 = [2,1,6,4,7,4,5]
# print(shell_sort(list1))

#bubble sort emmm.. 冒泡嘛你懂得 水压理解一下
def bubble_sort(lists):
    n = len(lists)
    for i in range(n):
        for j in range(1,n-i): #emm n-i后面排序完成了不需要了
            if lists[j-1] > lists[j]:
                lists[j-1],lists[j] = lists[j],lists[j-1]
    return lists

# list1 = [2,1,6,4,7,4,5]
# print(bubble_sort(list1))


# merge sort 这个思想就很nice 排序只是一个应用。。。。good （二分的办)chong
def mergeSort(arr):  #此乃分之
    if(len(arr)<2):
        return arr
    middle = len(arr)//2
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):  #此乃并之 （治之）
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result +=left[:] #改良一下 简洁粗暴
    result +=right[:]
    # while left:  #原理版  理解方便
    #     result.append(left.pop(0))
    # while right:
    #     result.append(right.pop(0))
    return result

# list1 = [2,1,6,4,7,4,5]
# print(mergeSort(list1))


##quick_sort   core idea 就是找到基准的在第几个 分之为前后
#基准的位置准确的知道就OK  所以从后向前世找小于基准  从前向后是找大于滴呀 原理版
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
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# list1 = [2,1,6,4,7,4,5]
# print(quickSort(list1))

#quick sort 原理版本
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
    return left

# list1 = [2,1,6,4,7,4,5]
# print(Quick_sort(list1))

#heap sort idea 就是不停的进行最大堆的排序（或者最小堆）

def adjust_heap(lists,i,size): # 对比父亲节点和孩子节点的大小
    #调整堆
    lchild = 2 * i +1
    rchild = 2 * i +2
    maxi = i
    if lchild < size and lists[maxi] < lists[lchild]:
        maxi = lchild
    if rchild <size and lists[maxi] < lists[rchild]:
        maxi = rchild
    if maxi != i:
        lists[maxi], lists[i] = lists[i], lists[maxi]
        adjust_heap(lists,maxi,size)

def build_heap(lists,size):#emmm 构建一下
    for i in range(int(size/2)-1,-1,-1):
        adjust_heap(lists,i,size)
    return lists

def heap_sort(lists):
    size = len(lists)
    build_heap(lists,size)
    for i in range(0,size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists,0,i)
    return lists

# list1 = [2,1,6,4,7,4,5]
# print(build_heap(list1,len(list1)))
# print(heap_sort(list1))

# count sort
def count_sort(arr,k):  #比较逗比浪费空间 k = max（a） ****负数不得行
    ## 对于每一个元素A[i]，确定小于a[i]的元素个数。
    # 所以直接可以把a[I]放到输出数组的相应位置上，比如有5个数小于a[i]，
    # 则a[i]应该放在输出数组的第六个位置上
    n = len(arr)
    b = [0 for i in range(n)]
    c = [0 for i in range(k+1)]
    for j in arr:
        c[j] = c[j] +1
    for i in range(1,len(c)):
        c[i] = c[i] +c[i-1]
    for j in arr:
        b[c[j]-1] = j
        c[j] -=1
    return b

# list1 = [2,1,6,4,7,4,5]
# k = max(list1)
# print(count_sort(list1,k))


# bucket_sort 把数组A划分为n个大小相同的区间（即桶），
# 每个子区间各自排序，最后合并。桶排序要求数据的分布必须均匀，
# 否则可能会失效。计数排序是桶排序的一种特殊情况，
# 可以把计数排序当成每个桶里只有一个元素的情况
def bucket_sort(a):
    buckets = [0] * ((max(a) - min(a)) + 1)  # 初始化桶元素为0
    for i in range(len(a)):
        buckets[a[i] - min(a)] += 1  # 遍历数组a，在桶的相应位置累加值
        print(buckets)
    b = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            b += [i + min(a)] * buckets[i]
    return b

# list1 = [2,-1,6,4,7,4,5]
# print(bucket_sort(list1))

## 基数排序
def radix_sort(lists,d=3):
    for i in range(d):
        s = [[] for k in range(10)]

        for j in lists:
            s[int(j/(10**i))%10].append(j)
        print(s)
        lists = [a for b in s for a in b]
    return  lists
list1 = [2,1,67,4,7,4,5]
print(radix_sort(list1,d=2))


