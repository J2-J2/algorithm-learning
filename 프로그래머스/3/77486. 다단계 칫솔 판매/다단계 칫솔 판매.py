def solution(enroll, referral, seller, amount):
    answer = []
    ret = [0] * len(enroll)
    order = {name : i for i, name in enumerate(enroll)}
    
    for i in range(len(seller)):
        cost = amount[i] * 100
        a = order[seller[i]]
        if referral[order[seller[i]]] == '-':
            ret[a] += cost * 0.9 // 1
            continue
        
        while True:
            if cost < 10: 
                ret[a] += cost
                break

            bcost = cost * 0.1 // 1
            acost = cost - bcost

            ret[a] += acost

            cost = bcost
            if referral[a] == '-':
                break
            a = order[referral[a]]
            
        
    return ret