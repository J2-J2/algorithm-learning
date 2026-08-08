def solution(n, l, r):
    answer = 0
    a = ((l-1) // 5) * 5
    b = ((r-1) // 5 + 1) * 5
    ls = [[a, b]]

    ret = "1"
    for i in range(n):
        a = a // 5
        b = b // 5+1 if b // 5 != 0 else 1
        ls.append([a, b])
    
    ls = list(reversed(ls))

    for i in range(n):
        a, b = ls[i]
        offset = ls[i-1][0] * 5 if i != 0 else 0
        ret = ret[a - offset:b-offset]
        ret = ret.replace("0", "00000")
        ret = ret.replace("1", "11011")
    a, b = ls[-1]
    ret = ret[l-1-a:r-a]

    return ret.count('1')

