def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    now = 0
    
    while now < n:
    
        for idx in range(n):
            progresses[idx] += speeds[idx]
        
        a = 0
        for jdx in range(now, n):
            if progresses[jdx] >= 100:
                a += 1
            else:
                break
        if a > 0:
            answer.append(a)
        now += a
    return answer