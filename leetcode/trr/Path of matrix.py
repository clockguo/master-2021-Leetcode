import copy

# def find(self, m, n, board, word):
#     print(word,'m',m,'\nn ',n)
#     if len(word)==0: return True
#     if m>=0 and m<len(board) and n>=0 and n<len(board[0]):
#         if m+1<len(board):
#             if board[m + 1][n] == word[0]:
#                 board[m+1][n] = None
#                 ans1=find(self, m + 1, n, board, word[1:])
#             else: ans1 = False
#         else:
#             ans1=False
#         if m-1>=0:
#             if board[m - 1][n] == word[0]:
#                 board[m - 1][n] = None
#                 ans2 = find(self, m - 1, n, board, word[1:])
#             else: ans2=False
#         else:
#             ans2 = False
#         if n+1<len(board[0]):
#             if board[m][n+1] == word[0]:
#                 board[m][n+1] = None
#                 ans3 = find(self, m , n+1, board, word[1:])
#             else: ans3 =False
#         else:
#             ans3 = False
#         if n-1>=0:
#             if board[m][n - 1] == word[0]:
#                 board[m][n-1] = None
#                 ans4 = find(self, m, n - 1, board, word[1:])
#             else: ans4 =False
#         else:
#             ans4 =False
#     if ans1 or ans2 or ans3 or ans4:
#         return True
#     else: return False

# def exist(board,word):
#     if len(board) == 0:
#         return False
#     if len(board[0])==0:
#         return False
#     board1=copy.deepcopy(board)
#
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == word[0]:
#                 # print(board,'\n',board1)
#                 board[i][j]=None
#                 ans = find(0,i,j,board,word[1:])
#                 board = copy.deepcopy(board1)
#                 if ans:
#                     return ans
#             else: ans = False
#
#     return ans
#
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"

# board = [["a","b"],["c","d"]]
# word = "abcd"

class Solution:
    def find(self, m, n, board, word,k):

        if m>=0 and m<len(board) and n>=0 and n<len(board[0]) and board[m][n]==word[k]:
            tem,board[m][n] = board[m][n],'-'
            ans1 = Solution.find(self, m + 1, n, board, word,k+1)
            ans2 = Solution.find(self, m - 1, n, board, word,k+1)
            ans3 = Solution.find(self, m , n+1, board, word,k+1)
            ans4 = Solution.find(self, m, n - 1, board, word,k+1)
            board[m][n] = tem
        else: return False
        if k==len(word)-1: return True
        if ans1 or ans2 or ans3 or ans4:
            return True
        else: return False
    def exist(self, board, word):
        if len(board) == 0:
            return False
        if len(board[0])==0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    ans = Solution.find(0,i,j,board,word,0)
                    if ans:
                        return ans
                else: ans = False
        return ans



board = [["A"]]
word = "AB"

print(board)
print(Solution.exist(0,board,word))
