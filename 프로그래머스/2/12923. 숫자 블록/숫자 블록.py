import math

def solution(begin, end):
    answer = [1] * (end - begin + 1)
    
    for i in range(end - begin + 1):
        if i+begin == 1: 
            answer[i] = 0
            continue
        idx = 2
        
        while True:
            if (i+begin) % idx == 0: 
                if (i+begin) // idx > 10000000:
                    answer[i] = idx
                else:
                    answer[i] = (i+begin) // idx
                    break

            if (i+begin)**0.5 < idx: 
                break
            idx += 1

        
    
    return answer