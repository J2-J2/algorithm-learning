from collections import defaultdict

def dfs(dic, k, infection, step):
    ret = 0
    if step == k:
        return max(ret, len(infection))
    
    for i in range(1, 4):
        temp = []
        
        while True:
            flag = 0
            for x, y in dic[i]:
                if x in infection and y not in infection: 
                    temp.append(y)
                    infection.add(y)
                    flag = 1
                elif y in infection and x not in infection: 
                    temp.append(x)
                    infection.add(x)
                    flag = 1
            if flag == 0: break
            
        
        for t in temp:
            infection.add(t)
        ret = max(dfs(dic, k, infection, step+1), ret)
        for t in temp:
            infection.remove(t)
    return ret
            


def solution(n, infection, edges, k):
    answer = 0
    dic = defaultdict(list)
    
    for x, y, t in edges:
        dic[t].append([x, y])
    a = set()
    a.add(infection)
    answer = dfs(dic, k, a, 0)
    return answer