from collections import Counter

def solution(weights):
    
    answer = 0
    cnt = Counter(weights)
    l = sorted(list(set(weights)))
    
    for weight in l:
        if cnt[weight] > 1: answer += (cnt[weight]*(cnt[weight]-1)) // 2
        if weight % 3 == 0:
            if weight // 3 * 4 in cnt:
                answer += (cnt[weight]*cnt[weight // 3 * 4])
        if weight % 2 == 0:
            if weight // 2 * 3 in cnt:
                answer += (cnt[weight]*cnt[weight // 2 * 3])
        if weight * 2 in cnt:
            answer += (cnt[weight]*cnt[weight * 2])           
    return answer