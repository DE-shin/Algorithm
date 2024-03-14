import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(19)]


dy = [0, 1, 1, 1]
dx = [1, 1, 0, -1]

def chk(y, x):
    return 0 <= y < 19 and 0 <= x < 19
    

def dfs(y, x, color):

    for i in range(4):
        cnt = 1
        pos = [(y, x)]
        
        idx = 0
        while True:
            idx += 1
            ny = y + dy[i] * idx
            nx = x + dx[i] * idx
            if not chk(ny, nx) or arr[ny][nx] != color:
                break
            
            elif chk(ny, nx) and arr[ny][nx] == color:
                cnt += 1
                pos.append((ny, nx))

        idx = 0
        while True:
            idx += 1
            ny = y - dy[i] * idx
            nx = x - dx[i] * idx
            if not chk(ny, nx) or arr[ny][nx] != color:
                break
            
            elif chk(ny, nx) and arr[ny][nx] == color:
                cnt += 1
                pos.append((ny, nx))

        if cnt == 5:
            pos.sort(key = lambda p:(p[1], p[0]))
            return True, pos[0]
            
    return False, (0, 0)
            


win = False
for y in range(19):
    for x in range(19):
        if arr[y][x] == 1 or arr[y][x] == 2:
            win, pos = dfs(y, x, arr[y][x])

        if win:
            break
    if win:
        break

if win:
    print(arr[y][x])
    print(pos[0] + 1, pos[1]+1)
else:
    print(0)