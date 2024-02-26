def solution(k, tangerine):
    answer = 0
    table = [0] * (10000001)
    for x in tangerine:
        table[x] += 1
    table.sort(reverse=True)

    for i in table:
        if k - i <= 0:
            answer += 1
            break
        k -= i
        answer += 1
        
    return answer