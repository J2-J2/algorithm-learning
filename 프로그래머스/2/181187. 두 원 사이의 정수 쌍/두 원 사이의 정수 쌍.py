def solution(r1, r2):
    cnt = 0

    for i in range(1, r2+1):
        h2 = (r2**2 - i**2) ** 0.5
        
        cnt += (int(h2) + 1)

    for i in range(1, r1):
        h1 = (r1**2 - i**2) ** 0.5
        cnt -= (int(h1) + 1)
        if i != r1 and h1 == int(h1): cnt += 1
            
            
    return cnt*4