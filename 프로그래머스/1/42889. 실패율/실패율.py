def solution(N, stages):
    answer = []
    cnt = [0] * (N+2)
    for x in stages:
        cnt[x] += 1

    failure = [-1] * (N+1)

    for i in range(1, N+1):
        if sum(cnt[i:]) == 0:
            for j in range(i, N+1):
                failure[j] = 0
            break
        else:
            failure[i] = (cnt[i]/sum(cnt[i:]))
    for j in range(N):
        answer.append(failure.index(max(failure)))
        failure[failure.index(max(failure))] = -1
    return answer