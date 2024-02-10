def solution(n):
    answer = 0
    division = 1234567
    table = [0] * (2001)
    table[1] = 1
    table[2] = 2
    
    if n >= 3:
        for i in range(3, n+1):
            table[i] = (table[i-1] + table[i-2]) % division
        
    answer = table[n]
    return answer