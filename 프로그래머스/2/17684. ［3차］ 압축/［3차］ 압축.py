def solution(msg):
    idx = 1
    num = 27
    answer = []
    temp = msg[0]
    dic = {chr(ord('A') + i): i+1 for i in range(26)}

    while idx != len(msg):
        temp += msg[idx]
        if temp not in dic:
            answer.append(dic[temp[:-1]])
            dic[temp] = num
            num+=1
            idx += 1
            temp = temp[-1]
        else:
            idx += 1
    answer.append(dic[temp])
    return answer