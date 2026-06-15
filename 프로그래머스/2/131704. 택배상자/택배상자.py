def solution(order):
    answer = 0
    belt = []
    box_idx = 1
    order_idx = 0
    while order_idx < len(order) and box_idx <= len(order):
        if box_idx > order[order_idx] and belt and belt[-1] != order[order_idx]: break
        
        belt.append(box_idx)
        while True:
            if belt and belt[-1] == order[order_idx]:
                answer += 1
                belt.pop()
                order_idx += 1
            else: break
        box_idx += 1
        
    return answer