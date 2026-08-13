def solution(n, stations, w):
    answer = 0
    
    ret = [1] + stations + [n]

    for i in range(len(ret)-1):
        temp = ret[i+1] - ret[i] - 1 - 2*w
        if i == 0 or i+1 == len(ret)-1:
            temp += w+1
        if temp <= 0: continue

        answer += temp // (2*w+1)
        if temp % (2*w+1) != 0: answer += 1


    return answer