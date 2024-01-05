def solution(lottos, win_nums):
    answer = []
    rand = lottos.count(0)
    cnt = 0
    for x in lottos:
        if x in win_nums:
            cnt += 1
    def ranking(x):
        if x < 2:
            return 6
        else:
            return 7 - x
    answer.append(ranking(cnt+rand))
    answer.append(ranking(cnt))
    return answer