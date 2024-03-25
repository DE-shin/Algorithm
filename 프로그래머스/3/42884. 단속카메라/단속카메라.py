def solution(routes):
    answer = 0
    start = -30001
    end = -30001
    routes = sorted(routes, key=lambda x:x[1])
    
    for s, e in routes:
        if s > end:
            answer += 1
            start = s
            end = e
        
    return answer