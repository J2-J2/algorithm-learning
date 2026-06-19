def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board[::-1]]
    
    while True:
        elim = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '0':
                    if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                        elim.update([(i, j), (i+1,j), (i, j+1), (i+1, j+1)])
                        
        if not elim: break
        for y, x in elim:
            board[y][x] = '0'
            
        for i in range(n):
            for j in range(m-1):
                if board[j][i] == '0': 
                    a = 1
                    while j + a < m:
                        if board[j+a][i] != '0': 
                            board[j][i], board[j+a][i] = board[j+a][i], board[j][i]
                            break
                        a += 1

    for i in range(m):
        for j in range(n):
            if board[i][j] == '0': answer += 1
            
    return answer