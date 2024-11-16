#! /usr/bin/env python3
def soln(board):
    rows = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j].isdigit():
                if board[i][j] in rows:
                    print("row same")
                    return False
                else:
                    rows[board[i][j]] = 1
        rows = {}

    cols = {}
    idx = 0
    for i in range(9):
        while idx<9:
            if board[idx][i].isdigit():
                if board[idx][i] in cols:
                    print("col same")
                    return False
                else:
                    cols[board[idx][i]] = 1
            idx += 1
        cols = {}
        idx = 0

    box = {}
    dirs = [[-1,-1],[-1,0],[-1,1],
            [0,-1], [0,0],[0,1],
            [1,-1],[1,0],[1,1]]
    points = [[1,1], [1,4], [1,7],
              [4,1], [4,4], [4,7],
              [7,1], [7,4], [7,7]]

    for point in points:
        y,x = point
        for dir in dirs:
            j,i = dir
            if board[y+j][x+i].isdigit():
                if board[y+j][x+i] in box:
                    print("box same")
                    return False
                else:
                    box[board[y+j][x+i]] = 1
        box = {}

    return True

'''
board = [["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]
'''

board =[["9",".",".","6",".",".",".",".","."],
        [".",".",".",".","6",".",".",".","."],
        [".",".",".",".",".","1",".","3","."],
        [".",".",".",".",".",".",".",".","8"],
        [".",".",".",".",".","8",".",".","."],
        [".",".",".","4",".",".","2",".","."],
        [".",".",".",".",".",".",".",".","1"],
        ["6",".",".",".","1",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
print(soln(board))
