import copy

def solution(n):
    answer = 0
    visited = [[0]*n for _ in range(n)]
    
    def dfs(n, step, visited):
        ret = 0
        if step == n: 
            ret += 1
            return ret

        for j in range(n):
            if visited[step][j] == 0:
                temp = attack(step, j, visited)
                for y, x in temp:
                    visited[y][x] = 1
                ret += dfs(n, step+1, visited)
                for y, x in temp:
                    visited[y][x] = 0
        return ret



    def attack(i, j, visited):
        ret = []

        for k in range(len(visited)):
            if visited[i][k] == 0: ret.append([i, k])
            if visited[k][j] == 0: ret.append([k, j])
            l1 = k - j + i
            l2 = -k+j+i
            if 0 <= l1 < len(visited) and visited[l1][k] == 0:
                ret.append([l1, k])
            if 0 <= l2 < len(visited) and visited[l2][k] == 0:
                ret.append([l2, k])
        return ret

    
    answer = dfs(n, 0, visited)
    
    return answer