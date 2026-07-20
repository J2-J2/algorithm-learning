
def solution(k, d):
    answer = 2*(d//k)+1
    
    for i in range(k, d, k):
        answer += (d**2 - i**2)**0.5//k
    
    return answer