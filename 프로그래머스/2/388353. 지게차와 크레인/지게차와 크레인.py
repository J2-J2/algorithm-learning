from collections import deque
def solution(storage, requests):
    answer = 0
    edge = set()
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0 , 0]
    matrix = [[""] * (len(storage[0])+2) for _ in range(len(storage)+2)]
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            matrix[i+1][j+1] = storage[i][j]
    for j in range(1, len(storage[0])+1):
        for i in [1, len(storage)]:
            edge.add((i,j))
    for i in range(2, len(storage)):
        for j in [1, len(storage[0])]:
            edge.add((i,j))
    def deleteChar(to_del):
        for i,j in to_del:
            edge.remove((i,j))
            q = deque([(i,j)])
            while q:
                x, y = q.popleft()
                for d in range(len(dx)):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 1<=nx<len(storage) and 1<=ny<=len(storage[0]):
                        if matrix[nx][ny] == " ":
                            matrix[nx][ny] = ""
                            q.append((nx,ny))
                        elif matrix[nx][ny] != "":
                            edge.add((nx,ny))
    for request in requests:
        to_del = set()
        if len(request) == 1:
            for i,j in edge:
                if matrix[i][j] == request:
                    to_del.add((i,j))
                    matrix[i][j]=""
            deleteChar(to_del)
        else:
            for i in range(1, len(storage)+1):
                for j in range(1, len(storage[0])+1):
                    if matrix[i][j] == request[0]:
                        matrix[i][j] = " "
                        if (i,j) in edge:
                            to_del.add((i,j))
            deleteChar(to_del)
    return sum([1 if matrix[i][j] != "" and matrix[i][j] != " " else 0 for i in range(1, len(storage)+1) for j in range(1, len(storage[0])+1)])