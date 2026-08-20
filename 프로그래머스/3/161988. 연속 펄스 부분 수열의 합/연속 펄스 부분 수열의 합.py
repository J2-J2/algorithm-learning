def check(psum):
    i = j = 0
    s = 0
    
    for b in range(len(psum)):
        temp = psum[b] - psum[j]
        if temp > 0:
            j = b
            s += temp
            
    for a in range(j):
        temp = psum[a] - psum[i]
        if temp < 0:
            i = a
            s -= temp
    return s


def solution(sequence):
    answer = 0
    perse = [1] * len(sequence)
    temp1 = [sequence[i]*-1 if i % 2 == 0 else sequence[i] for i in range(len(sequence))]
    temp2 = [sequence[i]*-1 if i % 2 != 0 else sequence[i] for i in range(len(sequence))]
    psum1 = [0]
    psum2 = [0]
    
    for i in range(len(sequence)):
        psum1.append(psum1[-1] + temp1[i])
        psum2.append(psum2[-1] + temp2[i])

    return max(check(psum1), check(psum2))