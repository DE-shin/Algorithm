import heapq
def solution(n, works):
    answer = 0
    hq = []
    for w in works:
        heapq.heappush(hq, -w)
    
    while n > 0:
        x = -heapq.heappop(hq)
        if x == 0:
            break
        
        if x > 0:
            x -= 1
            n -= 1
            
        heapq.heappush(hq, -x)
        
    for a in hq:
        answer += (a**2)
    
    return answer