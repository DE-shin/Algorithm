import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(1, i+1):
        if s[i-j] > s[i]:
            dp[i] = max(dp[i], dp[i-j] + 1)

print(n - max(dp))