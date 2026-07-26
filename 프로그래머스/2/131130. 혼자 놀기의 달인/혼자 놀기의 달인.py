def solution(cards):
    answer = 0
    ret = [[0, []]]
    visited = [0] * len(cards)
    for i in range(len(cards)):
        if visited[i] == 1: continue
        idx = i
        temp = []
        while True:
            visited[idx] = 1
            temp.append(cards[idx])
            if cards[cards[idx]-1] not in temp: idx = cards[idx]-1
            else: break
        ret.append([len(temp), temp])
    ret.sort(key=lambda x: -x[0])
    
    return ret[0][0] * ret[1][0]