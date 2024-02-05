import sys
input = sys.stdin.readline

n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * n

for now in range(n):
    nxt = now + tp[now][0]

    if nxt <= n:
        dp[now] += tp[now][1]

        if nxt < n:
            for after in range(nxt, n):
                dp[after] = max(dp[now], dp[after])

        

print(max(dp))