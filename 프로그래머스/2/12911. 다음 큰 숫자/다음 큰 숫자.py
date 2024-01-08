def solution(n):
    answer = 0
    
    def bin(x):
        b = ""
        while x > 1:
            b += str(x%2)
            x = x // 2
        b += "1"
        return b[::-1]
    
    c = bin(n).count("1")

    while True:
        n +=1 
        if bin(n).count("1") == c:
            answer = n
            break
    return answer