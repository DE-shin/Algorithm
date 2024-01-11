n, r, c = map(int, input().split())
answer = 0
while n > 0:
    r_s = c_s = (2**(n-1))

    if 0 <= r < r_s and 0 <= c < c_s:
        n -= 1
        
    elif 0 <= r < r_s and c >= c_s:
        answer += (2**n)*(2**n) // 4
        c = c - (2**(n-1))
        n -= 1

    elif r >= r_s and 0 <= c < c_s:
        answer += ((2**n)*(2**n) // 4) * 2
        r = r - (2**(n-1))
        n -= 1
        
    elif r >= r_s and c >= c_s:
        answer += ((2**n)*(2**n) // 4) * 3
        r = r - (2**(n-1))
        c = c - (2**(n-1))
        n -= 1
    
    r_s = r_s // 2
    c_s = c_s // 2

print(answer)