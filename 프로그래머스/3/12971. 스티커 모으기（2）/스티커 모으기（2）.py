def solution(sticker):
    answer = 0
    n = len(sticker)
    
    if n <= 1:
        return max(sticker)
    
    dp = [0] * (n)
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    
    dp_2 = [0] * (n)
    dp_2[1] = sticker[1]
    
    for i in range(2, n-1):
        dp[i] = max(sticker[i] + dp[i-2], dp[i-1])
        
    for i in range(2, n):
        dp_2[i] = max(sticker[i] + dp_2[i-2], dp_2[i-1])

    answer = max(max(dp), max(dp_2))
    return answer