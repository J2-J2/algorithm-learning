from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        first = heappop(scoville)
        second = heappop(scoville)
        new = first + second*2
        heappush(scoville, new)
        answer += 1
    
    return -1 if len(scoville) == 1 and scoville[0] < K else answer