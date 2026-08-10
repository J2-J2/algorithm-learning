from heapq import heappush, heappop, heapify

def solution(n, works):
    answer = 0
    heap = [-work for work in works]
    heapify(heap)
    for i in range(n):
        target = heappop(heap)
        target = min(target+1, 0)
        heappush(heap, target)
    return sum(work**2 for work in heap)