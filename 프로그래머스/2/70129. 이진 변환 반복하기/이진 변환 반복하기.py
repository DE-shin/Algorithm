def solution(s):
    answer = [0, 0]
    
    def binary(x):
        bin = ""
        while x !=1 :
            bin += str(x%2)
            x = x // 2
            
        bin += "1"
        return bin[::-1]
    
    while s != "1":
        answer[1] += s.count("0")
        s = s.replace("0", "")
        s = binary(len(s))
        print(s)
        answer[0] += 1
        
    return answer