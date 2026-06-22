from collections import deque
import math

def solution(storey):
    answer = 0
    i = 1
    while storey != 0:
        storey, d = divmod(storey, 10)
        if d < 5:
            answer += d
        elif d > 5:
            answer += (10 - d)
            storey += 1
        else:
            if storey % 10 >= 5:
                storey += 1
                answer += 5
            else:
                answer += 5
        
    
    
    return answer