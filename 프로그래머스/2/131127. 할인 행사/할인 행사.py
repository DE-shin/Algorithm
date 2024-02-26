from collections import Counter
def solution(want, number, discount):
    answer = 0
    d = {k:v for k, v in zip(want, number)}    

    for j in range(len(discount) - 9):
        n = True
        temp = discount[j:j+10]
        c = Counter(temp)
        for k, v in c.items():
            if k not in d or d[k] != v:
                n = False
                break
        if n:
            answer += 1
        
    return answer