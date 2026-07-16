def solution(plans):
    answer = []
    for i in range(len(plans)):
        time = list(map(int, plans[i][1].split(':')))
        time = time[0]*60 + time[1]
        plans[i][1] = time
        plans[i][2] = int(plans[i][2])
        
    plans = sorted(plans, key=lambda x: -x[1])
    targets = []
    for t in range(0, 1440):
        if targets: 
            targets[-1][2] -= 1
            if targets[-1][2] == 0: answer.append(targets.pop()[0])
        
        if plans and t == plans[-1][1]: targets.append(plans.pop())
            
    while targets:
        answer.append(targets.pop()[0])
    return answer