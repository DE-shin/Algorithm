import heapq
def solution(A, B):
    answer = 0
    heapq.heapify(A)
    heapq.heapify(B)
    
    while B:
        a = heapq.heappop(A)
        b = heapq.heappop(B)
        
        if a >= b:
            heapq.heappush(A, a)
        else:
            answer += 1
    return answer