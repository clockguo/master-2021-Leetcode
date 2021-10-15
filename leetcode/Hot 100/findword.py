
def exist(board, word: str):
    direct = [(0,-1),(0,1),(-1,0),(1,0)]
    cur = 0
    def BT(x,y,cur,mark):
        if len(word)-1==cur:
            return True
        # if word[cur] != board[x][y]:
        #     return False
        for direct1 in direct:
            x = x + direct1[0]
            y = y + direct1[1]

            if 0<=x<len(board) and 0<=y<len(board[0]) and mark[x][y] == False and  word[cur+1] == board[x][y]:
                mark[x][y] = True
                tem = BT(x,y,cur+1,mark)
                if tem:
                    return True
                else:
                    mark[x][y] = False
                    # cur -=1
            x = x - direct1[0]
            y = y - direct1[1]
        return False
    mark = [[False for _ in range(len(board[0]))] for ii in range(len(board))]
    print(board)
    print(len(board))
    print(mark)
    for i in range(len(board)):
        for j in range(len(board[0])):
            mark[i][j] = True
            if board[i][j] == word[cur]:
                if BT(i,j,cur,mark):
                    return True
            mark[i][j] = False
    return False

# board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

board = [["a"]]
word  ="a"
print(exist(board,word))