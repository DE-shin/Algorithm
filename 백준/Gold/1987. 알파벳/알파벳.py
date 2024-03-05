import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = set()


cnt = 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
    
def dfs(y, x, cost):
    global cnt

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if (0 <= ny < n and 0 <= nx < m) and (arr[ny][nx] not in visited):
            visited.add(arr[ny][nx])
            dfs(ny, nx, cost + 1)
            visited.discard(arr[ny][nx])

    cnt = max(cnt, cost)



visited.add(arr[0][0])
dfs(0, 0, 1)
print(cnt)