def solution(n, m, section):
    answer = 0
    painted = 0
    
    for x in section:
        if x > painted:
            # if end
            if x + m - 1 > n:
                answer += 1
                break
            else:
                painted = x+m-1
                answer += 1
        
    return answer