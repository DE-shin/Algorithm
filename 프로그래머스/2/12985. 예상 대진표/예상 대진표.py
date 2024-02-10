def solution(n,a,b):
    answer = 0
    
    def nxt_num(n):
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n // 2) + 1       
        return n

    while abs(a-b) >= 1:
        answer += 1
        a = nxt_num(a)
        b = nxt_num(b)

    return answer