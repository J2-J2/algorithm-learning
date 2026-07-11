from itertools import combinations

def dfs(q, step, ans, curr, answer, gg):
    if step >= len(q):
        if len(curr) == 5: 
            answer.add(tuple(sorted(curr)))
        elif len(curr) < 5:
            temp = []
            for c in curr:
                gg[c] = 1
            for i, g in enumerate(gg):
                if i == 0: continue
                if g == 0: temp.append(i)
            for c in curr:
                gg[c] = 0
            for combi in combinations(temp, 5 - len(curr)):
                answer.add(tuple(sorted(curr + list(combi))))
                
        return answer
    q_temp = []
    ret = set()
    pos = 5
    for i in q[step]:
        if i not in curr:
            pos -= 1
            if gg[i] == 0:
                q_temp.append(i)
                
    cnt = ans[step] - pos
    if cnt < 0 or len(q_temp) < cnt:
        return ret
    elif cnt == 0:
        for c in q_temp:
            gg[c] = 1
        ret.update(dfs(q, step+1, ans, curr, answer, gg))
        for c in q_temp:
            gg[c] = 0
    else:
        for combi in combinations(q_temp, cnt):
            for c in q_temp:
                if c not in combi:
                    gg[c] = 1
            ret.update(dfs(q, step+1, ans, curr+list(combi), answer, gg))
            for c in q_temp:
                if c not in combi:
                    gg[c] = 0
    return answer
            
            
            


def solution(n, q, ans):
    answer = 0
    s = set()
    gg = [0] * (n+1)
    answer = dfs(q, 0, ans, [], s, gg)
    return len(answer)