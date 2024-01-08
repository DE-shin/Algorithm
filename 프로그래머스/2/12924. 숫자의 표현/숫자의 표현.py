def solution(n):
    answer = 0
    
    i = 0
    x = 1
    while (n - i) // x > 0:
        if (n - i) % x == 0:
            answer += 1
            
        i += x
        x += 1
    return answer