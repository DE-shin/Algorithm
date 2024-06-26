import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = arr[i-1][0]
        v = arr[i-1][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])

print(max(dp[-1]))