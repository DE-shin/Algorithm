from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if arr[z][y][x] == 1:
                q.append((1, z, y, x))

dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

while q:
    day, z, y, x = q.popleft()

    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if arr[nz][ny][nx] == 0:
                arr[nz][ny][nx] = day + 1
                q.append((day+1, nz, ny, nx))

ans = 1
minus_one = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if arr[z][y][x] == 0:
                minus_one = 1
            ans = max(ans, arr[z][y][x])

if minus_one:
    print(-1)
else:
    print(ans-1)

