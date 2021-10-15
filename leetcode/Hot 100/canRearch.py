def canRearch1(arr,start):
    if tem[start]==1: return False
    else: tem[start] = 1
    if arr[start]==0: return True
    if arr[start]+start<len(arr):
        right=canRearch1(arr,start+arr[start])
    else:
        right = False
    if 0<=start-arr[start]:
        left = canRearch1(arr,start-arr[start])
    else:
        left = False
    return left or right

arr =  [3,0,2,1,2]
start = 0
tem = [0]*len(arr)
print(canRearch1(arr,start))
