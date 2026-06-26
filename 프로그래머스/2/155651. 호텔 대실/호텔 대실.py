from heapq import heappush, heappop

def time_diff(time, new_time):
    h, m = time
    nh, nm = new_time
    
    ret = (nh-h)*60 + (nm-m)
    if ret >= 0: return 1
    return 0

def solution(book_time):
    answer = 0
    heap = []
    book_time = sorted(book_time)
    for start, end in book_time:
        answer = max(answer, len(heap))
        start = list(map(int, start.split(':')))
        while heap and time_diff(heap[0], start):
            target = heappop(heap)
        end = list(map(int, end.split(':')))
        end[1] += 10
        heappush(heap, end)
            
    answer = max(answer, len(heap)) 
    return answer