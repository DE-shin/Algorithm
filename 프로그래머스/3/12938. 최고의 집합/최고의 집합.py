
def solution(n, s):
    if n > s:
        return [-1]
    
    answer = [s//n] * n
    s = s % n
    if s > 0:
        for i in range(s):
            answer[-(i+1)] += 1
            
    return answer