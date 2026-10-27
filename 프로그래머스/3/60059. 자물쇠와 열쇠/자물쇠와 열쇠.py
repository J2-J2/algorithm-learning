from copy import deepcopy

def solution(key, lock):
    n = len(key)
    m = len(lock)
    
    target = []
    for i in range(m):
        for j in range(m):
            if lock[i][j] == 0: target.append([i, j])
    
    copied_key = deepcopy(key)
    arrays = [copied_key]
    for i in range(3):
        copied_key = [list(temp) for temp in zip(*copied_key[::-1])]
        arrays.append(deepcopy(copied_key))
    
    for array in arrays:
        for i in range(-(n-1), m):
            for j in range(-(n-1), m):
                flag = True
                for q in range(m):
                    for w in range(m):
                        if q - i < 0 or q - i >= n or w - j < 0 or w - j >= n: 
                            value = 0
                        else:
                            value = array[q-i][w-j]
                        if lock[q][w] + value != 1: flag = False
                        if not flag: break
                    if not flag: break
                if flag == True: return True

    return False