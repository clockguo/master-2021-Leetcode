def minNumber(nums):
    list1 = []
    for i in nums:
        list1.append(str(i))
    i,j = 0,len(list1)-1
    def partition(left,rghit):
        if left>=rghit:return
        i , j =left , rghit
        while i < j:
            while list1[left]+list1[j]<= list1[j]+list1[left] and i<j: j -=1
            while list1[i] + list1[left] <= list1[j] + list1[left] and i < j: i += 1
            list1[i], list1[j] = list1[j], list1[i]
        list1[left], list1[j] = list1[j], list1[left]
        partition(left,i-1)
        partition(i+1,rghit)
        return
    partition(i,j)
    str1 = ''
    for i in list1:
        str1 += i
    return str1
nums = [3, 30, 34, 5, 9]
print(minNumber(nums))