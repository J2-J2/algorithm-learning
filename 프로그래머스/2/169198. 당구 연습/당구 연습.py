def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        temp = 1000000000000
        if y != n and startY != n and not (startX == x and y > startY):
            dist_x = abs(startX - x)
            dist_y = abs(n-startY) + abs(n-y)
            temp = min(temp, dist_x**2 + dist_y**2)
        if y != 0 and startY != 0 and not (startX == x and y < startY):
            dist_x = abs(startX - x)
            dist_y = abs(startY) + abs(y)
            temp = min(temp, dist_x**2 + dist_y**2)
        
        if x != m and startX != m and not (startY == y and x > startX):
            dist_x = abs(m - x) + abs(m - startX)
            dist_y = abs(startY - y)
            temp = min(temp, dist_x**2 + dist_y**2)
        if x != 0 and startX != 0  and not (startY == y and x < startX):
            dist_x = abs(x) + abs(startX)
            dist_y = abs(startY - y)
            temp = min(temp, dist_x**2 + dist_y**2)
        answer.append(temp)
        
    return answer