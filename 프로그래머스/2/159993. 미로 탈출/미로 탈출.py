
def bfs(visited, maps, queue, target):
    step = 0
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    while queue:
        next_step = []
        while queue:
            y, x = queue.pop()
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] in ['S', 'L', 'O', 'E'] and visited[ny][nx] == 0:
                    if maps[ny][nx] == target: return step + 1
                    next_step.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1
        step += 1
        queue = next_step
    
    return 0
    
def solution(maps):
    answer = 0
    visited1 = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited2 = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'L':
                lever = [i, j]
            elif maps[i][j] == 'S':
                start = [i, j]
    visited1[start[0]][start[1]] = 1
    visited2[lever[0]][lever[1]] = 1
    step1 = bfs(visited1, maps, [start], 'L')
    step2 = bfs(visited2, maps, [lever], 'E')
    
    
    return -1 if (step1 == 0 or step2 == 0) else step1+step2 