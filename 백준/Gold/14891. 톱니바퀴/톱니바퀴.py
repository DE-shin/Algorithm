gear = [list(map(int, input())) for _ in range(4)]
k = int(input())
rotate = [list(map(int, input().split())) for _ in range(k)]
answer = 0

def calc():
    global answer
    if gear[0][0] == 1:
        answer += 1
    if gear[1][0] == 1:
        answer += 2
    if gear[2][0] == 1:
        answer += 4
    if gear[3][0] == 1:
        answer += 8

# right [2] left [6]

def dfs(x, d):
    for i in range(-1, 2, 2):
        nx = x + i
        if 0 <= nx < 4:
            if table[nx] == 0:
                if i == -1:
                    if gear[x][6] != gear[x-1][2]:
                        table[x-1] = -d
                        dfs(x-1, -d)
    
                elif i == 1:
                    if gear[x][2] != gear[x+1][6]:
                        table[x+1] = -d
                        dfs(x+1, -d)


def rot(n, d):
    if d == 1:
        gear[n] = [gear[n][-1]] + gear[n][:-1]
    elif d == -1:
        gear[n] = gear[n][1:] + [gear[n][0]]


for number, direction in rotate:
    table = [0, 0, 0, 0]
    number -= 1
    table[number] = direction
    dfs(number, direction)

    for idx, t in enumerate(table):
        rot(idx, t)

calc()
print(answer)

