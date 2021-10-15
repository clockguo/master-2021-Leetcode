# def isEscapePossible(blocked, source, target):
#     if len(blocked) == 0:
#         return True
#
#     block = set((i, j) for i, j in blocked)
#
#     max_steps = len(blocked) * (len(blocked) - 1) // 2
#
#     def dfs(ii, jj, steps, target_i, target_j, visited):
#         if steps > max_steps:
#             return True
#
#         if ii < 0 or jj < 0:
#             return False
#         if (ii, jj) in block:
#             return False
#
#         if ii == target_i and jj == target_j:
#             return True
#
#         visited.add((ii, jj))
#         for new_i, new_j in [(ii + 1, jj), (ii - 1, jj), (ii, jj - 1), (ii, jj + 1)]:
#             if (new_i, new_j) in visited:
#                 continue
#
#             if dfs(new_i, new_j, steps + 1, target_i, target_j, visited):
#                 return True
#
#         return False
#
#     return dfs(source[0], source[1], 0, target[0], target[1], set()) and \
#            dfs(target[0], target[1], 0, source[0], source[1], set())
#
# print(isEscapePossible([[0, 0], [1, 1]],[1,0],[0,1]))

def isok(block,source,target,matrix):
    visit = []
    def DFS(x,y,target,visit):
        if x == target[0] and y == target[1]:
            return True
        if x not in range(0,len(matrix)) or y not in range(0,len(matrix[0])):
            return False
        if [x,y] in block or [x,y] in visit:
            return False
        visit.append([x,y])

        v1 = DFS(x-1,y,target,visit)
        v2 = DFS(x + 1, y, target, visit)
        v3 = DFS(x , y-1, target, visit)
        v4 = DFS(x, y+1, target, visit)
        if v1 or v2 or v3 or v4:
            return True
    return DFS(source[0],source[1],target,visit)


n = int(input())
for i in range(n):
    block = []
    line1 = list(map(int, input().split()))
    for left in range(line1[0]):
        line2 = input()
        for right in range(line1[1]):
            if line2[right] == '#':
                block.append([left,right])
            elif line2[right] == 'S':
                source = [left,right]
            elif line2[right] == 'E':
                target = [left,right]
            else: continue
    # print(block,source,target)
    maxt = [[0]*line1[1] for _ in range(line1[0])]
    if isok(block,source,target,maxt) == True:
        print('YES')
    else:
        print('NO')