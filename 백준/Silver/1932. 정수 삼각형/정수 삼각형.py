n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (i+1) for i in range(n)]
dp[0] = tri[0]
for i in range(n):
    for j in range(i+1):
        if dp[i][j] == 0:
            if j == 0:
                dp[i][j] = dp[i-1][j] + tri[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + tri[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tri[i][j]

print(max(dp[i]))            