from collections import deque
def solution(begin, target, words):
    answer = 0
    def count(a, b):
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt += 1
        return cnt
    
    if target not in words:
        return 0
    
    else:
        q = deque()
        q.append((begin, 0))
        
        while q:
            now, cost = q.popleft()
            if now == target:
                answer = cost
                break
            
            for w in words:
                if count(now, w) == 1:
                    q.append((w, cost+1))
            
    return answer