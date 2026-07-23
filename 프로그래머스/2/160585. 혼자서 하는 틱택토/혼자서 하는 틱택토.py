def check(board, mark):
    row = 0
    col = 0
    cross = 0

    for i in range(3):
        if board[0][i] == mark and board[1][i] == mark and board[2][i] == mark:
            col += 1
        if mark*3 == board[i]:
            row += 1
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark: cross += 1
    if board[2][0] == mark and board[1][1] == mark and board[0][2] == mark: cross += 1
    return row + col + cross
            

def solution(board):
    answer = 0
    a = check(board, 'O')
    b = check(board, 'X')
    a_cnt = 0
    b_cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O': a_cnt += 1
            if board[i][j] == 'X': b_cnt += 1
    if a_cnt - b_cnt == 0:
        if ((a, b) == (0, 1) or (a, b) == (0, 0)): answer = 1
        
    if a_cnt - b_cnt == 1:
        if ((a, b) == (1, 0) or (a, b) == (0, 0)): answer = 1
        if a_cnt == 5 and (a, b) == (2, 0): answer = 1
    return answer