import sys
input = sys.stdin.readline

n =int(input())
arr = list(int(input()) for _ in range(n))

t = [[(0, 0), (0, 0), (0, 0)] for _ in range(n)]
t[0] = [(0, 0), (arr[0], 1), (arr[0], 2)]


for i in range(1, n):
    for j in range(3):
        if j == 2:
            t[i][0] = max(t[i][0], (t[i-1][j][0], 0))
        elif j == 1:
            t[i][0] = max(t[i][0], (t[i-1][j][0], 0))
            t[i][2] = (t[i-1][j][0] + arr[i], 2)
        elif j == 0:
            t[i][0] = max(t[i][0], (t[i-1][j][0], 0))
            t[i][1] = (t[i-1][j][0] + arr[i], 1)

print(max(t[-1])[0])
            
