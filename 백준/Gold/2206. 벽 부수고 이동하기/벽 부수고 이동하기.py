from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[False, False] for _ in range(m)] for _ in range(n)]
ans = False
q = deque()
q.append((1, 0, 0, 0)) # dis, y, x, is 1
visited[0][0] = [True, True]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def chk(y, x):
    return 0 <= y < n and 0 <= x < m

while q:
    dis, y, x, wall = q.popleft()

    if y == n-1 and x == m-1:
        ans = True
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if chk(ny, nx):
            if wall == 0:
                if arr[ny][nx] == 1 and not visited[ny][nx][0]:
                    visited[ny][nx][0] = True
                    q.append((dis+1, ny, nx, 1))
                if arr[ny][nx] == 0 and not visited[ny][nx][0]:
                    visited[ny][nx][0] = True
                    q.append((dis+1, ny, nx, 0))
            elif wall == 1:
                if arr[ny][nx] == 0 and not visited[ny][nx][1]:
                    visited[ny][nx][1] = True
                    q.append((dis+1, ny, nx, 1))

if ans:
    print(dis)
else:
    print(-1)
            