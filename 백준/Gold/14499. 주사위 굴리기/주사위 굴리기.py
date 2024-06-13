n, m, y, x, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
arr = list(map(int, input().split()))
dice = [[0], [0, 0, 0], [0], [0]]


def turn(n):
    if n == 1:
        dice[1][0], dice[1][1], dice[1][2], dice[3][0] = dice[3][0], dice[1][0], dice[1][1], dice[1][2]
    elif n == 2:
        dice[1][0], dice[1][1], dice[1][2], dice[3][0] = dice[1][1], dice[1][2], dice[3][0], dice[1][0]
    elif n == 3:
        dice[0][0], dice[1][1], dice[2][0], dice[3][0] = dice[1][1], dice[2][0], dice[3][0], dice[0][0]
    elif n == 4:
        dice[0][0], dice[1][1], dice[2][0], dice[3][0] = dice[3][0], dice[0][0], dice[1][1], dice[2][0]

for dir in arr:
    ny = y; nx = x
    if dir == 1:
        nx = x + 1
    elif dir == 2:
        nx = x - 1
    elif dir == 3:
        ny = y - 1
    elif dir == 4:
        ny = y + 1

    if 0 <= ny < n and 0 <= nx < m:
        y = ny; x = nx

        if graph[y][x] == 0:
            turn(dir)
            graph[y][x] = dice[3][0]
        else:
            turn(dir)
            dice[3][0] = graph[y][x]
            graph[y][x] = 0
        print(dice[1][1])