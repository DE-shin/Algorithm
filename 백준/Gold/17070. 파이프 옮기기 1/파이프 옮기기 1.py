import sys
input = sys.stdin.readline

answer = 0
n = int(input())
graph = [list(input().split()) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(1, n):
        if graph[i][j] == '0':
            dp[i][j][0] += (dp[i][j-1][0] + dp[i][j-1][2])
            dp[i][j][1] += (dp[i-1][j][1] + dp[i-1][j][2])
        if graph[i][j] == '0' and graph[i-1][j] == '0' and graph[i][j-1] == '0':
            dp[i][j][2] += (dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2])

print(sum(dp[-1][-1]))