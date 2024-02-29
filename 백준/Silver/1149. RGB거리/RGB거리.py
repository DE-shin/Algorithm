import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n+1)]
dp[1] = arr[0]

for i in range(2, n+1):
    dp[i] = [min(dp[i-1][1], dp[i-1][2]) + arr[i-1][0], 
            min(dp[i-1][0], dp[i-1][2]) + arr[i-1][1],
            min(dp[i-1][0], dp[i-1][1]) + arr[i-1][2]]

print(min(dp[-1]))