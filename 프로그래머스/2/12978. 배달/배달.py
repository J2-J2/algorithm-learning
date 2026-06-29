from collections import defaultdict

def dfs(visited, dic, k, num, total):
    
    for target, score in dic[num]:
        if (visited[target] == 0 or visited[target] > total + score) and total + score <= k:
            visited[target] = total + score
            visited = dfs(visited, dic, k, target, total + score)
    return visited
            

def solution(N, road, K):
    answer = 0
    
    dic = defaultdict(list)
    for p1, p2, score in road:
        dic[p1].append([p2, score])
        dic[p2].append([p1, score])
    
    visited = [0] * (N+1)
    visited[1] = 1
    visited = dfs(visited, dic, K, 1, 0)
    for i in visited:
        if i != 0: answer += 1
    return answer