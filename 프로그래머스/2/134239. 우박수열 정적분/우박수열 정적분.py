def integral(start, end, values, n):
    ret = values[start] + values[n+end]
    for i in range(start+1, n+end):
        ret += values[i] * 2
    return ret / 2

def solution(k, ranges):
    values = [k]
    answer = []
    n = 0
    while k > 1:
        if k % 2 == 0: k = k // 2
        else: k = k * 3 + 1
        values.append(k)
        n += 1
    for start, end in ranges:
        if start == n + end: answer.append(0.0)
        elif start > n + end: answer.append(-1.0)
        elif start >= n: answer.append(0.0)
        else:
            if end > n: end = n
            answer.append(integral(start, end, values, n))
    return answer