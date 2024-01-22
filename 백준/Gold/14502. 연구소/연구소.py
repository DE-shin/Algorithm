from itertools import combinations
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
blank = []
virus = []
wall = []
ans = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))
        else:
            wall.append((i, j))


def dfs(y, x):
    visited[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 1 and graph[ny][nx] == 0:
            dfs(ny, nx)

for w1, w2, w3 in combinations(blank, 3):
    # 3 new walls
    graph[w1[0]][w1[1]] = 1
    graph[w2[0]][w2[1]] = 1
    graph[w3[0]][w3[1]] = 1

    # dfs for virus
    result = 0
    visited = [[1] * (m) for _ in range(n)]
    for by, bx in virus:
        dfs(by, bx)

    # check blank number
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                result += 1
    result -= len(wall)
    result -= 3
    # check the maximum space
    ans = max(ans, result)

    # restore graph
    graph[w1[0]][w1[1]] = 0
    graph[w2[0]][w2[1]] = 0
    graph[w3[0]][w3[1]] = 0

print(ans)



