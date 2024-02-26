import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]

def chk(A, B):
    for y in range(n):
        for x in range(m):
            if A[y][x] != B[y][x]:
                return False
    return True

def rev(arr, y, x):
    for i in range(3):
        for j in range(3):
            if arr[y+i][x+j] == 0:
                 arr[y+i][x+j] += 1
            else:
                 arr[y+i][x+j] -= 1
    return arr

cnt = 0

for y in range(n-2):
    for x in range(m-2):
        if a[y][x] != b[y][x]:
            a = rev(a, y, x)
            cnt += 1
           
if not chk(a, b):
    cnt = -1

print(cnt)
            