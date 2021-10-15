data=[]
for a in range(9):
    c=a
    b=d=8-a
    data.append([a,b,c,d])
for i in data:
    for j in i:
        print(j,end=' ')
    print()