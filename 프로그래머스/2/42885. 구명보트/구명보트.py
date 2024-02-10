from collections import deque

def solution(people, limit):
    answer = 0

    q = deque(sorted(people))
    
    while q:
        r = q.pop()
        l = 0
        answer += 1
        if q:
            l = q.popleft()
            
        if r + l <= limit:
            pass
        else:
            q.appendleft(l)
    return answer