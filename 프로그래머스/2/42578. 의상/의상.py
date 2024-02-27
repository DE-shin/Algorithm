from collections import defaultdict
def solution(clothes):
    answer = 1
    d = defaultdict(int)
    for x in clothes:
        d[x[-1]] += 1
    for k, v in d.items():
        answer *= (v+1)
    answer -=1
    return answer