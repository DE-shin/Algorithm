from collections import defaultdict
def solution(genres, plays):
    answer = []
    d = defaultdict(int)
    for g, p in zip(genres, plays):
        d[g] += p
    d = dict(sorted(d.items(), key = lambda x:x[1], reverse=True))
    for genre in d:
        temp = []
        for i in range(len(genres)):
            if genre == genres[i]:
                temp.append((i, plays[i]))
        temp.sort(key = lambda x: x[1], reverse=True)
        i = 0
        for t in temp:
            if i == 2:
                break
            answer.append(t[0])
            i += 1
    return answer