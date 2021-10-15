def maxslidewindow(nums,k):
    if k==1: return nums
    j,i = 1,0
    maxt, maxid= [nums[0]],[0]
    ans = []
    while j<len(nums):
        if maxid[0]<j-k+1:
            maxt.pop(0)
            maxid.pop(0)
        if nums[j]<=maxt[-1]:
            maxt.append(nums[j])
            maxid.append(j)
        else:
            for i in maxt[::-1]:
                if nums[j]>i:
                    maxt.pop()
                    maxid.pop()
                else: break
            maxt.append(nums[j])
            maxid.append(j)
        if j>=k-1:
            ans.append(maxt[0])
        j+=1
    return ans

nums = [1,3,1,2,0,5]
k =3
print(maxslidewindow(nums,k))


