n = int(input())
for _ in range(n):
    m = int(input())
    temp = []
    Flag = True
    for _ in range(m):
        temp_list = list(map(int,input().split()))

        temp_list = xz(temp_list)
        if temp_list in temp:
            Flag = False
            print("YES")
            break
        else:
            temp.append(temp_list)
    if Flag:
        print("NO")
    def xz(arr):
        min1 = min(arr)
        for i in range(len(arr)):
            if arr[i] == min1:
                return arr[i:]+arr[:i]

