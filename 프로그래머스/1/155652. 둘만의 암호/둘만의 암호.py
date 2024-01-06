def solution(s, skip, index):
    answer = ''
    
    alpha = list(map(chr, range(97, 123)))
    for d in skip:
        alpha.remove(d)
        
    for l in s:
        answer += alpha[(alpha.index(l) + index) % (26 - len(skip))]
    return answer