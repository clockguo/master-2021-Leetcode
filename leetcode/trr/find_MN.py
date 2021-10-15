
# def find_number(matrix,target):
#     M = len(matrix)
#     if M == 0:
#         return False
#     N = len(matrix[0])
#     if N == 0:
#         return False
#     if target > matrix[M - 1][N - 1] or target < matrix[0][0]:
#         return False
#     if target == matrix[M - 1][N - 1] or target == matrix[0][0]:
#         return True
#
#     for i in range(min(M,N)):
#         if min(M,N)==1:
#             break
#         if target == matrix[M - i - 2][N - i - 2]:
#             return True
#         elif target > matrix[M-i-2][N-i-2]:
#             for j in range(M-i-1):
#                 if matrix[j][N-i-1]==target:
#                     return True
#                 elif matrix[j][N-i-1]>target:
#                     break
#                 elif matrix[j][N-i-1]<target:
#                     continue
#             for j in range(N-i-1):
#                 if matrix[M-i-1][j]==target:
#                     return True
#                 elif matrix[M-i-1][j]>target:
#                     break
#                 elif matrix[M-i-1][j]<target:
#                     continue
#             return False
#         else:
#             continue
#     if M==N:
#         return False
#     elif M>N:
#         for i in range(M-N+1):
#             if target == matrix[i][0]:
#                 return True
#             elif target>matrix[i][0]:
#                 continue
#             else:
#                 break
#         return False
#     else:
#         for i in range(N-M + 1):
#             if target == matrix[0][i]:
#                 return True
#             elif target > matrix[0][i]:
#                 continue
#             else:
#                 break
#         return False

def find_number(matrix,target):
    M,N=len(matrix)-1,0
    while M>=0 and N<len(matrix[0]):
        if matrix[M][N]==target:
            return True
        elif matrix[M][N]<target:
            N +=1
        elif matrix[M][N]>target:
            M -=1
    return False



matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
matrix1=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

# print(len(matrix1[0]))

OUtcome= find_number(matrix,5)
print(OUtcome)