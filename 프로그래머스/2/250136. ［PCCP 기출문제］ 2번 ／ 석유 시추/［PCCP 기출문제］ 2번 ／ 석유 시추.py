from collections import defaultdict
import sys
sys.setrecursionlimit(10000000)

def dfs(y, x, land, visited, num):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    visited[y][x] = num
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < len(land) and 0 <= nx < len(land[0]) and land[ny][nx] == 1 and visited[ny][nx] == 0:
            dfs(ny, nx, land, visited, num)
    

def solution(land):
    answer = 0
    visited = [[0] * len(land[0]) for _ in range(len(land))]
    num = 1
    for i in range(len(land)):
        for j in range(len(land[0])):
            if visited[i][j] == 0 and land[i][j] == 1: 
                dfs(i, j, land, visited, num)
                num += 1
               

    dic = defaultdict(int)
    for i in range(len(land)):
        for j in range(len(land[0])):    
            if visited[i][j] != 0:
                dic[visited[i][j]] += 1
    
    for j in range(len(land[0])):
        temp = set()
        cnt = 0
        for i in range(len(land)):  
            if land[i][j] == 1 and visited[i][j] != 0:
                temp.add(visited[i][j])
        for t in temp:
            cnt += dic[t]
        answer = max(answer, cnt)
    return answer