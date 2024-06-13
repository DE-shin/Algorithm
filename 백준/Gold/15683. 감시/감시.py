n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = n*m
cctv = []
for y in range(n):
    for x in range(m):
        if 1 <= graph[y][x] <= 5:
            cctv.append((y, x, graph[y][x])) # y, x type

def draw(y, x, direction, turn):
    for dir in direction:
        dir += turn
        ny = y; nx = x
        if dir % 4 == 0:
            while nx < m-1 and graph[ny][nx] != 6:
                nx += 1
                if graph[ny][nx] <= 0:
                    graph[ny][nx] -= 1
        elif dir % 4 == 1:
            while ny < n-1 and graph[ny][nx] != 6:
                ny += 1
                if graph[ny][nx] <= 0:
                    graph[ny][nx] -= 1
        elif dir % 4 == 2:
            while 0 < nx  and graph[ny][nx] != 6:
                nx -= 1
                if graph[ny][nx] <= 0:
                    graph[ny][nx] -= 1
        elif dir % 4 == 3:
            while 0 < ny  and graph[ny][nx] != 6:
                ny -= 1
                if graph[ny][nx] <= 0:
                    graph[ny][nx] -= 1

def undraw(y, x, direction, turn):
    for dir in direction:
        dir += turn
        ny = y; nx = x
        if dir % 4 == 0:
            while nx < m-1 and graph[ny][nx] != 6:
                nx += 1
                if graph[ny][nx] <= -1:
                    graph[ny][nx] += 1
        elif dir % 4 == 1:
            while ny < n-1 and graph[ny][nx] != 6:
                ny += 1
                if graph[ny][nx] <= -1:
                    graph[ny][nx] += 1
        elif dir % 4 == 2:
            while 0 < nx  and graph[ny][nx] != 6:
                nx -= 1
                if graph[ny][nx] <= -1:
                    graph[ny][nx] += 1
        elif dir % 4 == 3:
            while 0 < ny  and graph[ny][nx] != 6:
                ny -= 1
                if graph[ny][nx] <= -1:
                    graph[ny][nx] += 1

def calc():
    global answer
    res = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 0:
                res += 1
    answer = min(answer, res)
            
def dfs(idx):
    if idx == len(cctv):
        calc()
        return

    y = cctv[idx][0]; x = cctv[idx][1]; type = cctv[idx][2]

    if type == 1:
        j = 4; direction = [0]
    elif type == 2:
        j = 2; direction = [0, 2]
    elif type == 3:
        j = 4; direction = [0, 1]
    elif type == 4:
        j = 4; direction = [0, 1, 2]
    elif type == 5:
        j = 1; direction = [0, 1, 2, 3]

    for i in range(j):
        draw(y, x, direction, i)
        dfs(idx + 1)
        undraw(y, x, direction, i)


dfs(0)
print(answer)