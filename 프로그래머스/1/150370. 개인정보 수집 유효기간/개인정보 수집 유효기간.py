def solution(today, terms, privacies):
    answer = []
    ty, tm, td = map(int, today.split("."))
    t_total = ty * 28 * 12 + tm * 28 + td
    expire_list = dict()
    
    for expire_info in terms:
        expire_type, expire_date = expire_info.split()
        expire_list[expire_type] = int(expire_date) * 28
        
    for i, privacy in enumerate(privacies):
        ny, nm, nd = map(int, privacy[:-2].split("."))
        n_total = ny * 28 * 12 + nm * 28 + nd
        
        if n_total + expire_list[privacy[-1]] <= t_total:
            answer.append(i+1)
    
    return answer