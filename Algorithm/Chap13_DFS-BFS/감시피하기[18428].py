# 18428
import sys
from copy import deepcopy
from itertools import combinations

N = int(sys.stdin.readline())
stu_len = 0

graph = []
teacher_position = []
x_position = []

for i in range(N):
    graph.append(list(map(str, sys.stdin.readline().strip().split())))

    for j in range(N):
        if graph[i][j] == 'S':
            stu_len += 1
        elif graph[i][j] == 'T':
            teacher_position.append((i, j))
        else:
            x_position.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(copy_graph, x, y):
    for i in range(4):
        nx, ny = x, y

        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N or copy_graph[nx][ny] == 'O':
                break
            
            copy_graph[nx][ny] = 'T'

    return copy_graph

answer = 'NO'

for x_pos in list(combinations(x_position, 3)):
    copy_graph = deepcopy(graph)

    for data in x_pos:
        copy_graph[data[0]][data[1]] = 'O'

    for teacher in teacher_position:
        x, y = teacher[0], teacher[1]
        copy_graph = solution(copy_graph, x, y)

    compare_stu_len = 0

    for i in range(N):
        for j in range(N):
            if copy_graph[i][j] == 'S':
                compare_stu_len += 1
    
    if compare_stu_len == stu_len:
        answer = 'YES'
        break

print(answer)