import sys
sys.setrecursionlimit(10**9)
def dfs(y, x, visited, maps):
    ret = 0
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and visited[ny][nx] == 0 and maps[ny][nx] != 'X':
            visited[ny][nx] = 1
            ret += int(maps[ny][nx])
            ret += dfs(ny, nx, visited, maps)
    return ret
    

def solution(maps):
    answer = []
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                temp = int(maps[i][j])
                visited[i][j] = 1
                temp += dfs(i, j, visited, maps)
                answer.append(temp)
    return [-1] if len(answer) == 0 else sorted(answer)