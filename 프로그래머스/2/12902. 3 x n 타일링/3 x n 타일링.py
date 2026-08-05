def solution(n):
    answer = 3
    if n % 2 == 1: return 0

    k = n // 2    
    temp = [1] * (k+1)
    temp[1] = 3
    for i in range(2, k+1):
        value = 3 * temp[i-1] % 1000000007
        for j in range(0, i-1):
            value += 2 * temp[j] % 1000000007
        temp[i] = value % 1000000007

    return temp[-1]  % 1000000007