def solution(n):
    path = [0] * (n + 2)
    path[0] = 1
    div = 1000000007
    for i in range(n):
        path[i+1] = (path[i+1] + path[i]) % div
        path[i+2] = (path[i+2] + path[i]) % div

    return path[n]