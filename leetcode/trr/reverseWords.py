def reverseWords(s):
    i = len(s)-1
    ans = ''
    while i>-1:
        if s[i] == ' ': pass
        else:
            for j in range(i,-1,-1):
                if s[j] == ' ':
                    ans +=s[j+1:i+1]+' '
                    i = j
                    break
                elif j<=0:
                    ans +=s[j:i+1]+' '
                    i = j
                    break
        i -= 1
    return ans[:-1]
s = "a"
print(reverseWords(s))