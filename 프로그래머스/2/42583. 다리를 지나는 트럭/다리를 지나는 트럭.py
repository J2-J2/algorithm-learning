from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0] * bridge_length)
    idx = 0
    val = 0
    while idx < len(truck_weights):
        temp = queue.popleft()
        val -= temp
        
        if truck_weights[idx] + val <= weight:
            queue.append(truck_weights[idx])
            val += truck_weights[idx]
            idx += 1
        else:
            queue.append(0)
        if val != 0: answer += 1
        
    answer += bridge_length
    return answer