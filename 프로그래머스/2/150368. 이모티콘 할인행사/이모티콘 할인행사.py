

def solution(users, emoticons):
    answer = [0, 0]
    
    def dfs(step, emoticons, users, result):
    
        if step == len(emoticons):
            a = b = 0
            for i in range(len(users)):
                temp = 0
                for j in range(len(result)):
                    if result[j][0] >= users[i][0]:
                        temp += result[j][1]
                if temp >= users[i][1]: a += 1
                else: b += temp
            if a >= answer[0]: 
                if a != answer[0]: answer[1] = 0
                answer[0] = a
                if b >= answer[1]: answer[1] = b
            return

        for i in [10, 20, 30, 40]:
            temp = (emoticons[step] * (100 - i)) // 100
            result.append([i, temp])
            dfs(step + 1, emoticons, users, result)
            result.pop()
        
    dfs(0, emoticons, users, [])

        
    return answer