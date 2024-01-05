from collections import Counter
def solution(participant, completion):
    answer = ''

    runner = Counter(participant)
    complete = Counter(completion)

    for x in runner:
        if runner[x] - complete[x] != 0:
            answer = x
        
    return answer