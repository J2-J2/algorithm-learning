from collections import defaultdict

def bfs(n, graph, prev, log):
    visited = [0] * (n+1)
    visited[prev[0]] = 1
    idx = 0
    while prev:
        idx += 1
        cur = []
        for i in prev:
            for j in graph[i]:
                if visited[j] == 0:
                    log[j] = idx
                    visited[j] = 1
                    cur.append(j)
        prev = cur

    
    
            
def solution(n, roads, sources, destination):
    answer = []
    log = [0] * (n+1)
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    log = [-1] * (n+1)
    log[destination] = 0
    bfs(n, graph, [destination], log)
    
    return [log[i] for i in sources]