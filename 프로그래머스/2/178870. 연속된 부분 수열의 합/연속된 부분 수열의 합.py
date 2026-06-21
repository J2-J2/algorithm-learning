def solution(sequence, k):
    answer = [0, 1e9]
    acum = [0] + sequence
    for i in range(1, len(acum)):
        acum[i] = acum[i-1] + acum[i]
    
    i = 0
    j = 1
    while j != len(acum):
        if acum[j] - acum[i] == k:
            if answer[1] - answer[0] > j - i - 1:
                answer = [i, j-1]
            i += 1
            if i == j: break
        elif acum[j] - acum[i] > k: i += 1
        elif acum[j] - acum[i] < k: j += 1
    return answer