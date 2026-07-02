from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    heap = []
    
    for i in range(len(enemy)):
        
        
        if n - enemy[i] < 0:
            if k == 0: break
            heappush(heap, -enemy[i])
            n -= heappop(heap)
            k -= 1
            n -= enemy[i]
        
        else:
            n -= enemy[i]
            heappush(heap, -enemy[i])
        answer += 1
        
    return answer