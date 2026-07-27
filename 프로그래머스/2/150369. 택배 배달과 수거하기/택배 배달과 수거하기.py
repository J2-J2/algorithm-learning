def delivery(li, cap):
    result = []
    li = sorted([ [d, idx+1]for idx, d in enumerate(li)], key=lambda x: x[1])
    
    while li:
        temp = cap
        ret = 0
        while li:
            if li[-1][0] == 0: 
                li.pop()
                if not li and ret != 0: result.append(ret)
                continue
            if li[-1][0] > temp: 
                li[-1][0] -= temp
                ret = max(ret, li[-1][1])

                result.append(ret)
                break
            elif li[-1][0] <= temp:
                temp -= li[-1][0]
                ret = max(ret, li[-1][1])
                li.pop()
                if temp == 0 or not li: 
                    result.append(ret)
                    break
    return result


def solution(cap, n, deliveries, pickups):
    answer = 0
    de = sorted(delivery(deliveries, cap))
    pi = sorted(delivery(pickups, cap))


    while de or pi:
        d = p = 0
        
        if de: 
            d = de[-1]
            de.pop()
        if pi: 
            p = pi[-1]
            pi.pop()
        answer += max(d, p)*2

    return answer