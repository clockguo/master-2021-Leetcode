
def trap(height):
    T1max,T1xid,T2max,T2xid = 0,0,0,0
    i,j = 0,len(height)-1
    sum = 0

    while i<=j:
        if T1max <T2max:
            if height[i] > T1max:
                T1max = height[i]
                if T2max < T1max: continue
            else:
                sum += T1max -height[i]
            i = i+1
        if T1max >= T2max:
            if height[j] > T2max :
                T2max = height[j]
                if T2max>T1max: continue
            else:
                sum += T2max -height[j]
            j = j-1

    return sum


height = [2,0,2]
print(trap(height))