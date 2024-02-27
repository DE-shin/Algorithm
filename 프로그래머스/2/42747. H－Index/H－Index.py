def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    start = 0
    end = n
    while start <= end:
        mid = (start + end) // 2
        
        v = mid
        while v not in citations:
            v += 1
            if v > citations[-1]:
                break
        if v in citations:
            num = n - citations.index(v)
        else:
            num = 0
        
        if mid <= num:
            start = mid + 1
        
        else:
            end = mid - 1
            
    answer = end
    return answer