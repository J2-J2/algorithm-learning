from collections import deque
def solution(x, y, n):
    answer = 0
    queue = deque([[x]])
    if x == y: return 0
    visited = [0] * (y+1)
    
    while queue:
        target = queue.popleft()
        ret = []
        for i in target:
            for j in [i + n, i*2, i*3]:
                if j <= y and visited[j] == 0:
                    ret.append(j)
                    visited[j] = 1
        answer += 1
        if ret:
            queue.append(ret)
        if y in ret: return answer
        
    return -1