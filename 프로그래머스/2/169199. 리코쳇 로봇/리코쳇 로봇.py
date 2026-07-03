def solution(board):
    answer = 0
    ny = nx = -1
    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    queue = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                visited[i][j] = 1
                queue.append([i, j])
    
    while queue:
        
        temp = []
        
        for y, x in queue:
            for i in range(4):
                ny = y
                nx = x
                while 0 <= (ny + dy[i]) < len(board) and 0 <= (nx + dx[i]) < len(board[0]) and board[ny + dy[i]][nx + dx[i]] != 'D':
                    ny = ny + dy[i]
                    nx = nx + dx[i]
                if (ny != y or nx != x) and visited[ny][nx] == 0:
                    if board[ny][nx] == 'G': return answer + 1
                    visited[ny][nx] = 1
                    temp.append([ny, nx])
        queue = temp
        answer += 1
    return -1