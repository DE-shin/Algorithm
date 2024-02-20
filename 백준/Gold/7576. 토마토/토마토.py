from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque()
for y in range(n):
    for x in range(m):
        if tomato[y][x] == 1:
            q.append((y, x))
day = 0
def bfs():
    while q:
        y, x = q.popleft()
        
    
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
    
            if 0 <= ny < n and 0 <= nx < m:
                if tomato[ny][nx] == 0:
                    q.append((ny, nx))
                    tomato[ny][nx] = tomato[y][x] + 1

bfs()
answer = 1
for y in range(n):
    for x in range(m):
        if tomato[y][x] == 0:
            print(-1)
            exit()
        else:
            answer = max(answer, tomato[y][x])

print(answer - 1)
