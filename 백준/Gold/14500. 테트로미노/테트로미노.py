import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# Check
def chk(y, x):
    return 0 <= y < n and 0 <= x < m

# Square
def f1(y, x):
    t = 0
    for i in range(2):
        for j in range(2):
            if chk(y+i, x+j):
                t += arr[y+i][x+j]
            else:
                return 0
    return t

# Line
def f2(y, x):
    t = 0
    for i in range(4):
        if chk(y, x+i):
            t += arr[y][x+i]
        else:
            return 0
    return t

def f3(y, x):
    t = 0
    for i in range(4):
        if chk(y+i, x):
            t += arr[y+i][x]
        else:
            return 0
    return t

# 3*2
def f4(y, x):
    t = 0
    if chk(y+2, x+1):
        a = []
        b = []
        for i in range(3):
            a.append(arr[y+i][x])
            b.append(arr[y+i][x+1])
        t = max(sum(a) + max(b), sum(b) + max(a))
        c = arr[y][x] + arr[y+1][x] + arr[y+1][x+1] + arr[y+2][x+1]
        d = arr[y][x+1] + arr[y+1][x+1] + arr[y+1][x] + arr[y+2][x]
        t = max(t, c, d)
    else:
        return 0
    return t

# 2*3
def f5(y, x):
    t = 0
    if chk(y+1, x+2):
        a = []
        b = []
        for i in range(3):
            a.append(arr[y][x+i])
            b.append(arr[y+1][x+i])
        t = max(sum(a) + max(b), sum(b) + max(a))
        c = arr[y][x] + arr[y][x+1] + arr[y+1][x+1] + arr[y+1][x+2]
        d = arr[y+1][x] + arr[y+1][x+1] + arr[y][x+1] + arr[y][x+2]
        t = max(t, c, d)
    else:
        return 0
    return t
    

for y in range(n):
    for x in range(m):
        answer = max(answer, f1(y, x))
        answer = max(answer, f2(y, x))
        answer = max(answer, f3(y, x))
        answer = max(answer, f4(y, x))
        answer = max(answer, f5(y, x))

print(answer)