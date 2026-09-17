from collections import defaultdict, deque
from heapq import heappush, heappop
INF = float('inf')

def bfs(a, dic, nodes):
    
    nodes[a][1] = 0
    queue = [(0,  a)]
    
    temp = []
    while queue:

        cost, target = heappop(queue)
        
        if cost > nodes[target][1]: continue
        
        for no, fa in dic[target]:
            new_cost = cost + fa
            
            if new_cost < nodes[no][1]: 
                nodes[no][1] = new_cost
                heappush(queue, (new_cost, no))
        
        
def solution(n, s, a, b, fares):
    answer = INF
    dic = defaultdict(list)
    for c, d, f in fares:
        dic[c].append([d, f])
        dic[d].append([c, f])
        
        
    nodes_a = [[[], INF] for _ in range(n+2)]
    bfs(a, dic, nodes_a)
    
    nodes_b = [[[], INF] for _ in range(n+2)]
    bfs(b, dic, nodes_b)
    
    nodes_c = [[[], INF] for _ in range(n+2)]
    bfs(s, dic, nodes_c)
    
    for i in range(1, n+1):
        answer = min(answer, nodes_c[i][1] + nodes_a[i][1] + nodes_b[i][1])
        
    return answer