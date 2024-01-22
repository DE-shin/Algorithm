import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, fx, fy = map(int, input().split())
# after s second, graph[fx-1][fy-1]
time = 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
q = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            q.append((i, j, graph[i][j], time))

q = deque(sorted(q, key=lambda x: x[2]))
while q:
    y, x, virus, time = q.popleft()
    if time > s:
        break

    for direction in range(4):
        ny = y + dy[direction]
        nx = x + dx[direction]

        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] == 0:
                graph[ny][nx] = virus
                time += 1
                q.append((ny, nx, virus, time))

print(graph[fx-1][fy-1])

