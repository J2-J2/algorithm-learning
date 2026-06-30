from collections import deque
from heapq import heappush, heappop

def solution(players, m, k):
    answer = 0
    heap = []
    
    for i, player in enumerate(players):
        
        while heap:
            if heap[0] <= i: heappop(heap)
            else: break
        
        if player // m > len(heap):
            for _ in range(player // m - len(heap)):
                heappush(heap, i+k)
                answer += 1
        
    
    
    return answer