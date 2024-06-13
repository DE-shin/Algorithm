from itertools import combinations
def solution(k, n, reqs):
    answer = int(1e9)
    
    mentors = [[] for _ in range(k+1)]
    for comb in combinations(range(1, n), k-1):
        if k > 1:
            e = 0
            for idx,s in enumerate(comb):
                mentors[idx+1] = [0] * (s-e)
                e = s
            mentors[-1] = [0] * (n-s)

        elif k:
            mentors[1] = [0] * (n)
        # main
        result = 0
        for t_start, t_lapse, typ in reqs:
            v = min(mentors[typ])
            idx = mentors[typ].index(v)

            if v <= t_start:
                mentors[typ][idx] = t_start + t_lapse

            else:
                result += (mentors[typ][idx] - t_start)
                mentors[typ][idx] += t_lapse

        answer = min(answer, result)
                
        
    return answer