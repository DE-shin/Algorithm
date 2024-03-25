def solution(n, stations, w):
    answer = 0
    idx = 1
    
    for x in stations:
        start = x - w
        end =  x + w
        
        if idx < start:
            answer += (start-idx) // (w*2 + 1)
            if (start - idx) % (w*2 + 1) != 0:
                answer += 1
        idx = end + 1
        
    if idx <= n:
        answer += (n -idx + 1) // (w*2 + 1)
        if (n - idx + 1) % (w*2 + 1) != 0:
            answer += 1
    return answer