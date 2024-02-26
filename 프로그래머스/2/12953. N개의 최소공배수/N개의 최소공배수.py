def solution(arr):
    answer = 1
    
    def prime():
        prime_list = []
        p = [True] * 101
        for i in range(2, 101):
            if p[i]:
                prime_list.append(i)
            
            for j in range(100//i + 1):
                p[i*j] = False
        
        return prime_list
    
    p = prime()
    d = {v: 0 for v in range(1, 101)}
    
    for x in arr:
        t = []
        while x not in p and x != 1:
            for y in p:
                if x % y == 0:
                    x = x // y
                    t.append(y)
        t.append(x)
        td = {primes : 0 for primes in set(t)}
        for i in t:
            td[i] += 1
            
        for x, y in td.items():
            d[x] = max(d[x], y)
    
    for i, j in d.items():
        if j != 0:
            answer = answer * (i ** j)
    return answer