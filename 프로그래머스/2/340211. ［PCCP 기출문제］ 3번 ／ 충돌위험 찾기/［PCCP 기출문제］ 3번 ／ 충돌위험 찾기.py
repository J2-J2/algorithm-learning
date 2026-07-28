def solution(points, routes):
    answer = 0
    maps = [[0]*100 for _ in range(100)]
    points = [[i-1, j-1] for i, j in points]
    robots = [points[r[0]-1][:] for r in routes]

    routes = [list(reversed(r))[:-1] for r in routes]

    for i, j in robots:
        maps[i][j] += 1
        
    for i in range(100):
        for j in range(100):
            
            if maps[i][j] > 1: 
                print('d')
                answer += 1
            
    while routes:
        temp = []
        
        for i in range(len(routes)):
            if not routes[i]: 
                maps[robots[i][0]][robots[i][1]] -= 1
                temp.append(i)
                continue
            target = points[routes[i][-1]-1]
            cur = robots[i]
            maps[cur[0]][cur[1]] -= 1
 
            if target != cur:
                if target[0] != cur[0]:
                    cur[0] += 1 if (target[0] - cur[0]) > 0 else -1
                elif target[1] != cur[1]:
                    cur[1] += 1 if (target[1] - cur[1]) > 0 else -1
                maps[cur[0]][cur[1]] += 1
            
                if target == cur: 
                    routes[i].pop()

        
        if temp:
            for t in sorted(temp, reverse=True):
                routes.pop(t)
                robots.pop(t)
                
        for i in range(100):
            for j in range(100):
                if maps[i][j] > 1: 

                    answer += 1
                
    return answer