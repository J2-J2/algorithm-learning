from itertools import permutations
import re

def solution(expression):
    answer = 0
    expression = re.split(r'([+*-])', expression)
    
    ex_list = []
    for i in permutations(['*', '-', '+'], 3):
        dic = {c: j for j, c in enumerate(i)}
        ret = []
        stack = []
        idx = 0
        
        while idx < len(expression):
            if expression[idx] in ['*', '-', '+']:
                while stack:
                    if dic[expression[idx]] >= dic[stack[-1]]:
                        ret.append(stack.pop())
                    else: 
                        break

                stack.append(expression[idx])
                idx += 1
            else:
                ret.append(expression[idx])
                idx += 1
        while stack:
            ret.append(stack.pop())
        ex_list.append(ret)
            
    for r in ex_list:
        temp = []
        for i in range(len(r)):
            
            if r[i] in ['*', '-', '+']:
                first = str(temp.pop())
                second = str(temp.pop())
                temp.append(eval(''.join(second+r[i]+first)))
            else: temp.append(r[i])
            
        answer = max(answer, abs(temp[0]))
        
    return answer