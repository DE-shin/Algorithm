import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, l, r = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

answer = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]

# inside check
def check(y, x):
    return 0 <= y < n and 0 <= x < n

def dfs(y, x):
    global group_sum
    group.append((y, x))
    group_sum += g[y][x]
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if check(ny, nx) and not visited[ny][nx]:
            if l <= abs(g[y][x] - g[ny][nx]) <= r:
                dfs(ny, nx)
                

while True:
    movement = []
    visited = [[False] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            group = []
            group_sum = 0
            if not visited[y][x]:
                dfs(y, x)
                if len(group) >= 2:
                    movement.append((group, group_sum))

    if len(movement) == 0:
        break
    
    for move_group, move_sum in movement:
        for my, mx in move_group:
            g[my][mx] = move_sum // len(move_group)
            
    answer += 1
    
print(answer)