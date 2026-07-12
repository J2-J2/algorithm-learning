import sys
sys.setrecursionlimit(100000)

def dfs(visited, storage, i, j, target):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    temp = []
    visited[i][j] = 1
    
    for k in range(4):
        ni = i + dy[k]
        nj = j + dx[k]
        
        if 0 <= ni < len(storage) and 0 <= nj < len(storage[0]) and visited[ni][nj] == 0:
            if storage[ni][nj] == target:
                temp.append([ni, nj])
            if storage[ni][nj] == '.':
                temp += dfs(visited, storage, ni, nj, target)
    return temp
    


def solution(storage, requests):
    answer = 0

    storage = [list(r) for r in storage]
    
    find = []
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            if i in [0, len(storage)-1] or j in [0, len(storage[0])-1]:
                find.append([i, j])
    
    for k in range(len(requests)):
        target = requests[k]
        temp = []
        
        if len(target) == 1:
            visited = [[0 for _ in range(len(storage[0]))] for _ in range(len(storage))]
            
            for i, j in find:
                if storage[i][j] == target: temp.append([i, j])
                elif storage[i][j] == '.' and visited[i][j] == 0: 
                    
                    temp += dfs(visited, storage, i, j, target)
                
                        
        else:
            for i in range(len(storage)):
                for j in range(len(storage[0])):
                    if storage[i][j] == target[0]:
                        temp.append([i, j])
        for i, j in temp:
            storage[i][j] = '.'
        
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            if storage[i][j] != '.': answer += 1
    
    return answer