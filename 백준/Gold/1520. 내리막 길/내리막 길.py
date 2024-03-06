import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = [[-1] * m for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def chk(y, x):
    return 0 <= y < n and 0 <= x < m

def dfs(y, x):
    

    if (y == n-1) and (x == m-1):
        return 1

    if cnt[y][x] == -1:
        cnt[y][x] = 0     
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
    
            if chk(ny, nx) and arr[ny][nx] < arr[y][x]:
                
                cnt[y][x] += dfs(ny, nx)
                
    return cnt[y][x]

print(dfs(0, 0))
