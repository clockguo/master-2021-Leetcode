def strToInt(str):
    i, j = 0, 1
    if not str: return 0
    if len(str)==1 and '0'<=str[0]<='9': return int(str[0])
    elif not '0' <= str[0] <= '9' and len(str)==1:return 0
    if not '0' <= str[0] <= '9' and str[0] != '-' and str[0] != ' 'and str[0] !='+': return 0
    for i in range(len(str)):
        if str[i] == ' ':
            i+=1
            continue
        elif not '0' <= str[i] <= '9' and str[i] != '-'and str[i] != '+':
            return 0
        else:
            if str[i]=='+' and i+1<len(str):
                str = str[i+1:]
                if not '0' <= str[0] <= '9': return 0
                break
            str = str[i:]

            print(str)
            break
    if len(str)==1 and '0'<=str[0]<='9': return int(str[0])
    elif not '0' <= str[0] <= '9' and len(str)==1:return 0
    if str[0] == '-' and not '0' <= str[1] <= '9': return 0
    i = 0
    while True:
        if '0' <= str[i] <= '9' and j < len(str):
            if not '0' <= str[j] <= '9':
                return min(int(str[i:j]), pow(2, 31)-1)
            if j + 1 >= len(str):
                return min(int(str[i:j + 1]), pow(2, 31)-1)
            j += 1
        elif str[i] == '-'and j < len(str):
            if not '0' <= str[j] <= '9':
                return max(-int(str[i + 1:j]), -pow(2, 31))
            if j + 1 >= len(str):
                return max(-int(str[i + 1:j + 1]), -pow(2, 31))
            j += 1
        else:
            i += 1
        if i >= len(str):
            break
    return 0

a =  "21474836489"
print(strToInt(a))