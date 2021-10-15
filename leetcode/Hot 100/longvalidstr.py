def long(s):
    stack = [-1]
    max1 = 0
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if stack!=[]:
                max1 =max(max1,i-stack[-1])
            else:
                stack.append(i)
    return max1

s = "(())()(()(("
print(long(s))