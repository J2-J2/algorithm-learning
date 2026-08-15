from heapq import heappush, heappop

def solution(n, s):
    answer = []
    
    heap = [s]
    
    if n > s: return [-1]


    a, b = divmod(s, n)
    answer = [a] * (n)
    
    for i in range(n-1, n-b-1, -1):
        answer[i] += 1

    return answer