from heapq import heappush, heappop
from collections import defaultdict

def solution(operations):
    answer = []
    up_cnt = 0
    down_cnt = 0
    
    up_stream = []
    down_stream = []
    dic = defaultdict(int)
    
    for o in operations:
        if o[0] == 'D':
            if len(o) == 3:
                stream = down_stream
                sign = -1
            elif len(o) == 4:
                stream = up_stream
                sign = 1
            
            while stream:
                temp = heappop(stream) * sign
                if dic[temp] != 0: 
                    dic[temp] -= 1
                    break
                    
        elif o[0] == "I":
            target = int(o.split()[1])
            dic[target] += 1
            heappush(up_stream, target)
            heappush(down_stream, -target)
    
    lefted = sorted([d for d in dic if dic[d] != 0])
    return [lefted[-1], lefted[0]] if lefted else [0, 0]