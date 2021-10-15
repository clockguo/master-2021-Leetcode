def minWindow(s,t):
    dic= {}
    for i in t:
        if i in dic:
            dic[i] +=1
        else: dic[i] =1
    left, right = 0,0
    ans = ''
    count = len(t)
    while right <len(s):
        if s[right] in dic:
            dic[s[right]] -=1
            if dic[s[right]] >=0:
                count -=1
        right +=1
        while count ==0:
            if ans == '' or len(ans)>(right-left):
                ans = s[left:right]
            if s[left] in dic:
                dic[s[left]] +=1
                if dic[s[left]] >0:
                    count +=1
            left +=1
    return ans

S = "cabwefgewcwaefgcf"

T = "cae"
print(minWindow(S,T))


