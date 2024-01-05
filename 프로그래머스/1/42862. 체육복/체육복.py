def solution(n, lost, reserve):
    answer = 0
    cnt = [1] * (n+2)
    cnt[0] = cnt[n+1] = -1
    for idx_lost in lost:
        cnt[idx_lost] -= 1
    for idx_res in reserve:
        cnt[idx_res] += 1
        
    for i, val in enumerate(cnt):
        if val == 0:
            if cnt[i-1] == 2:
                cnt[i-1] = 1
                cnt[i] = 1
                continue
            elif cnt[i+1] == 2:
                cnt[i+1] = 1
                cnt[i] = 1
    for x in cnt:
        if x > 0:
            answer += 1
    return answer