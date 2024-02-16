import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
group = [[0] * n for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def ChkIn(y, x):
    return 0 <= y < n and 0 <= x < n

def dfs(y, x, gnum):
    visited[y][x] = True
    group[y][x] = gnum

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ChkIn(ny, nx) and not visited[ny][nx] and graph[ny][nx] == "1":
            dfs(ny, nx, gnum)
            
gnum = 1
for i in range(n):
    for j in range(n):
        
        if graph[i][j] == "1" and not visited[i][j]:
            dfs(i, j, gnum)
            gnum += 1
            
answer = []
answer.append(gnum-1)
quantity = [0] * (gnum-1)

for i in range(n):
    for j in range(n):
        if group[i][j]:
            quantity[group[i][j]-1] += 1

answer += sorted(quantity)
for x in answer:
    print(x)

        