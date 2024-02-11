n, k = map(int, input().split())
coins = [int(input().strip()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1


for c in coins:
    for i in range(c, k+1):
        dp[i] += dp[i-c]

print(dp[-1])