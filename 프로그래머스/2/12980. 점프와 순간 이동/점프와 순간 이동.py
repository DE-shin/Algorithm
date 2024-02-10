def solution(n):
    ans = 0
    
    while n >= 1:
        if n == 1:
            ans += 1
            break
        elif n % 2 == 1:
            n -= 1
            ans += 1
        else:
            n = n // 2
    
    return ans