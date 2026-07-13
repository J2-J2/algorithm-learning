import math
def solution(w,h):
    
    n = math.gcd(w, h)
    a = w // n
    b = h // n
    
    cnt = 0
    y = 0
    for i in range(1, a):
        cnt += int((b*i) / a) - int(y) + 1
        y = (b*i) / a
        
    cnt += int(b) - int(y)
    
    return w*h - cnt*n