from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    orders = [sorted(order) for order in orders]
    
    for i in course:
        dic = defaultdict(int)
        for order in orders:
            if i > len(order): continue
            for combi in combinations(order, i):
                dic[combi] += 1
        if len(dic) == 0: continue
        max_order = max(list(dic.values()))
        if max_order < 2: continue
        for d in dic:
            if dic[d] == max_order: answer.append("".join(d))
    
            
    return sorted(answer)