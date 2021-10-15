import re
lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
tem = lines[-2]
a = ''
for i in range(int(tem),10):
    a +=str(i)
lines1 = lines[:]
ans = []
for i in lines[:-2]:
    for j in a:
        i = re.sub(j,'',i)
    ans.append(i)
i = lines[-1]
for j in a:
    i = re.sub(j,'',i)
ans.append(i)
res = []
for i in range(len(ans)-1):
    if ans[-1] in ans[i]:
        res.append(i)
for i in res:
    print(lines[i])


print(ans)
print(lines)