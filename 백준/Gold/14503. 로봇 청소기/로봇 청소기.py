import sys
input = sys.stdin.readline

n, m = map(int, input().split())
y, x, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cleaned = []
cnt = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def chk_in(y, x):
    return 0 <= y < n and 0 <= x < m

def turn(i):
    i -= 1
    return i % 4
    
while True:
    back = True
    if arr[y][x] == 0 and (y, x) not in cleaned:
        cnt += 1
        cleaned.append((y, x))
    
    else:
        for _ in range(4):
            d = turn(d)
            ny = y + dy[d]
            nx = x + dx[d]

            if chk_in(ny, nx):
                if arr[ny][nx] == 0 and (ny, nx) not in cleaned:
                    cnt += 1
                    cleaned.append((ny, nx))
                    back = False
                    y = ny
                    x = nx
                    break

        if back:
            by = y - dy[d]
            bx = x - dx[d]
    
            if chk_in(by, bx):
                if arr[by][bx] != 1:
                    y = by
                    x = bx
                else:
                    break
            else:
                break

 
print(cnt)