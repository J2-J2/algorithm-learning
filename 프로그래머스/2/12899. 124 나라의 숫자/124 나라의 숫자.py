def solution(n):
    num = []
    dic = {0:'4', 1:'1', 2:'2'}
    while n > 0:
        a, b = divmod(n, 3)
        if b == 0: a-=1
        num.append(dic[b])
        n = a
        
    return "".join(num[::-1])