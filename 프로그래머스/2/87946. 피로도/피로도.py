from itertools import permutations
def solution(k, dungeons):
    answer = -1
    
    for combi in permutations(dungeons, len(dungeons)):
        total = k
        cnt = 0
        for least, consumption in combi:
            if total >= least:
                total -= consumption
                cnt += 1
            answer = max(answer, cnt)
    return answer