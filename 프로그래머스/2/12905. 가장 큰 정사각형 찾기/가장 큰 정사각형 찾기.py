def solution(board):
    answer = 0
    sum_board = [ i[:] for i in board ]
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1: sum_board[i][j] = min(sum_board[i-1][j-1], sum_board[i-1][j], sum_board[i][j-1]) + 1

    return max(max(i) for i in sum_board) ** 2