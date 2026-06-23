from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
def dfs(n, dic, node, visited, a, b):
    
    for i in dic[node]:
        if visited[i] == 0 and not (node in [a, b] and i in [a, b]):
            visited[i] = 1
            dfs(n, dic, i, visited, a, b)
            
    
def solution(n, wires):
    answer = 1e9
    dic = defaultdict(list)
    for a, b in wires:
        dic[a].append(b)
        dic[b].append(a)
        
    for a, b in wires:
        visited = [0] * (n+1)
        dfs(n, dic, 1, visited, a, b)
        val = sum(visited)
        answer = min(answer, abs(n-2*val))
    return answer