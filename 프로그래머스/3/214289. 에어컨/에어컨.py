# 에어컨 ON -> 실내 온도 따라감 -> 다르면 a 같으면 b 소모
# 에어컨 OFF -> 실외 온도 따라감 -> 0 소모
# 실내 온도 t1 ~ t2 if 승객 있으면

# 첫번째 1 나오기 전까지 -> 무조건 에어컨 가동해서 목표 안으로 안착

def solution(temperature, t1, t2, a, b, onboard):
    n = len(onboard)
    answer = a*n

    dp =[[a*n] * 51 for _ in range(n)]

    dp[0][temperature+10] = 0

    def show():
        for rrrr in dp:
            print(rrrr[t1+9:t2+12])
        print()

    last_human = 0
    for l in range(n):
        if onboard[l] == 1:
            last_human = l
            
    for i in range(1, n):
        for j in range(51):
            if j == 0: # first case
                u = int(1e9)

                # temp same
                if temperature + 10 == j:
                    s = dp[i-1][j]
                else:
                    s = dp[i-1][j] + b
                    
                # temp down
                if temperature + 10 <= j:
                    d = dp[i-1][j+1]
                else:
                    d = dp[i-1][j+1] + a

            elif j == 50: # last case
                # temp up
                if temperature + 10 >= j:
                    u = dp[i-1][j-1]
                else:
                    u = dp[i-1][j-1] + a

                # temp same
                if temperature + 10 == j:
                    s = dp[i-1][j]
                else:
                    s = dp[i-1][j] + b

                d = int(1e9)

            else: # mid case
                # temp up
                if temperature + 10 >= j:
                    u = dp[i-1][j-1]
                else:
                    u = dp[i-1][j-1] + a

                # temp same
                if temperature + 10 == j:
                    s = dp[i-1][j]
                else:
                    s = dp[i-1][j] + b
                    
                # temp down
                if temperature + 10 <= j:
                    d = dp[i-1][j+1]
                else:
                    d = dp[i-1][j+1] + a
                    
            # dp calc
            dp[i][j] = min(u, s, d)
            if onboard[i] == 1:
                if not (t1 + 10 <= j <= t2 + 10):
                    dp[i][j] = int(1e9)

    answer = min(dp[last_human][t1+10: t2+11])

    return answer