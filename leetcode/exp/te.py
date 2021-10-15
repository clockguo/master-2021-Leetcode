# line = list(map(int, input().split()))
# # line1 = []
# # for i in range(line[1]):
# #     m = int(input())
# #     line1.append(m)
# # ans = 0
# # for i in range(line[1]):
# #     ans += line[0] // line1[i]
# # nums = [1]
# # for i in line1:
# #     nums += [tem*i for tem in nums]
# # nums.remove(1)
# # for i in line1:
# #     nums.remove(i)
# # print(nums)
# # res = 0
# # for i in nums:
# #     res += line[0]//i
# # if 1 in line1:
# #     print(line[0])
# # else:
# #     print(ans-res)

# def maxPathSum(grid):
#     dp = [[0 for _ in range(len(grid[0]))] for _ in range(2)]
#     dp[0][0] = grid[0][0]
#     for i in range(1, len(grid[0])):
#         dp[0][i] = dp[0][i - 1] + grid[0][i]
#     for i in range(1, len(grid)):
#         for j in range(len(grid[0])):
#             if j == 0:
#                 dp[1][j] = grid[i][j] + dp[0][j]
#             else:
#                 dp[1][j] = max(dp[0][j], dp[1][j - 1]) + grid[i][j]
#         dp[0] = dp[1][:]
#
#     return dp[0][-1]
# line = list(map(int, input().split()))
# grid = []
# for i in range(line[0]):
#     line1 = list(map(int, input().split()))
#     grid.append(line1)
# print(maxPathSum(grid))


def py_nms(dets, thresh):

    x1 = [x[0] for x in dets]
    y1 = [x[1] for x in dets]
    x2 = [x[2] for x in dets]
    y2 = [x[3] for x in dets]
    scores = [x[4] for x in dets]
    areas = []
    for i in range(len(x1)):
        areas1 = (x2[i] - x1[i] + 1) * (y2[i] - y1[i] + 1)
        areas.append(areas1)
    dice = {}
    for i in range(len(scores)):
        dice[scores[i]] = i
    scores.sort()[::-1]
    order = []
    for i in scores:
        order = dice[i]
    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)

        xx1 = max(x1[i], x1[order[1:]])
        yy1 = max(y1[i], y1[order[1:]])
        xx2 = min(x2[i], x2[order[1:]])
        yy2 = min(y2[i], y2[order[1:]])


        w = max(0.0, xx2 - xx1 + 1)
        h = max(0.0, yy2 - yy1 + 1)
        inter = w * h

        ovr = inter / (areas[i] + areas[order[1:]] - inter)
        print(ovr)

        # inds = where(ovr <= thresh)[0]
        inds = ovr[0]

        order = order[inds + 1]
    return keep

line = list(map(float, input().split()))
grid = []
for i in range(int(line[0])):
    line1 = list(map(float, input().split()))
    grid.append(line1)
det = py_nms(grid,line[1])
print(grid[det])