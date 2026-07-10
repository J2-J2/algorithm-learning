from collections import defaultdict

def solution(diffs, times, limit):
    time_total = 0
    answer = 0
    
    dic = defaultdict(int)
    for idx, (diff, time) in enumerate(zip(diffs, times)):
        if idx == 0: 
            level = diff
            time_total = time
        else:
            dic[diff] += times[idx-1]+time
            time_total += time

    left = 1
    right = 100000

    while True:
        mid = (left + right) // 2
        tt = 0
        for d in dic:
            if d - mid > 0: tt += (d - mid)*dic[d]
        
        if time_total + tt <= limit: right = mid
        else: left = mid +1
        
        if left == right:
            answer = left
            break
        
        
    return answer