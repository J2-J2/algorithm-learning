from itertools import combinations

def solution(relation):
    answer = 0
    
    atts = []
    ret = []
    cols = [i for i in range(0,len(relation[0]))]

    for i in range(1, len(relation[0])+1):
        atts.extend(list(combinations(cols, i)))
    
    for keys in range(len(atts)):
        temp = set()
        
        for i in range(len(relation)):
            tup = []
            for k in atts[keys]:
                tup.append(relation[i][k])
            temp.add(tuple(tup))
        if len(temp) == len(relation): ret.append(atts[keys])

    ret_tm = set()
    for i in range(len(ret)):
        for j in range(len(ret)):
            if i == j: continue
            check = 0
            for k in ret[i]:
                if k in ret[j]: check += 1
            if check == len(ret[i]):
                ret_tm.add(j)

    return len(ret) - len(ret_tm)