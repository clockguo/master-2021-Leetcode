def maxtri(heights):
    stack = []
    left, right = 0, 0
    count, maxm = 0, 0
    length = len(heights)
    while stack != [] or right < length:
        if stack==[]:
            stack.append(right)
            right +=1
            continue
        if right<length and heights[stack[-1]] <= heights[right]:
            stack.append(right)
            right += 1
        else:
            h = stack.pop()
            if stack==[]:left = 0
            else: left = stack[-1]+1
            count = right - left
            if maxm < count * heights[h]:
                maxm = count * heights[h]
    return max(maxm,length*left)

heights = [2,1,5,6,2,3,1,1,1,1,1,1,11,1,1,1,1,1,11,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(maxtri(heights))