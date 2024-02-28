import heapq
def solution(priorities, location):
    answer = 0
    r = list(range(len(priorities)))
    
    while priorities:
        m = max(priorities)
        
        if priorities[0] == m:
            
            if r[0] == location:
                answer += 1
                break
            priorities.pop(0)
            r.pop(0)
            answer += 1
        else:
            priorities.append(priorities.pop(0))
            r.append(r.pop(0))
                           
                
    return answer