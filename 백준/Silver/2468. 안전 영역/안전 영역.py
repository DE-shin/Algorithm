import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


max_terrain = 0
for y in range(n):
    for x in range(n):
        max_terrain = max(max_terrain, arr[y][x])
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x, limit):
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n:
            if not visited[ny][nx] and arr[ny][nx] > limit:
                dfs(ny, nx, limit)

ans = 0

for limit in range(max_terrain + 1):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if not visited[y][x] and arr[y][x] > limit:
                dfs(y, x, limit)
                cnt += 1
    
    ans = max(ans, cnt)

print(ans)