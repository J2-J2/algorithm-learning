from collections import defaultdict

def solution(picks, minerals):
    
    answer = 0
    table = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    dic1 = {"diamond": 25, "iron": 5, "stone": 1}
    dic2 = {"diamond": 0, "iron": 1, "stone": 2}
    
    cnt = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    cnt = cnt[:sum(picks)]
    
    for c in range(len(cnt)):
        temp = 0
        for i in cnt[c]:
            temp += dic1[i]
        cnt[c].append(temp)
    for c in sorted(cnt, key=lambda x: -x[-1]):
        for i in range(len(picks)):
            if picks[i] != 0:
                for j in range(len(c)-1):
                    answer += table[i][dic2[c[j]]]
                picks[i] -= 1
                break
    
    
    
    return answer