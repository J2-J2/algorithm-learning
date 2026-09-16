def solution(scores):
    answer = 0
    lim = 0
    temp = []
    scores = [[i, j, idx] for idx, (i, j) in enumerate(scores)]
    for i, j, idx in sorted(scores, key=lambda x: [-x[0], x[1]]):
        if j >= lim:
            lim = j
            temp.append([i+j, idx])
    

    temp = sorted(temp, reverse=True)
    prev = temp[0][0]
    cnt = 0
    for i, j in temp:
        if i == prev:
            cnt += 1
        else:
            answer += cnt
            cnt = 1
            prev = i
            
        if j == 0: 
            return answer+1
   
    return -1