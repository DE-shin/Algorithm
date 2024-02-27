from collections import deque
def solution(n, left, right):
    answer = []
    
    ly = left // n
    lx = left % n
    ry = right // n
    rx = right % n
    
    for i in range(ly, ry+1):
        temp = [i+1 for _ in range(i)]
        for j in range(1, n-i+1):
            temp.append(i+j)
            
        if ly == ry:
            answer += temp[lx:rx+1]
            
        elif i == ly:
            answer += temp[lx:]
        elif i == ry:
            answer += temp[:rx+1]
        else:
            answer += temp
    
    
    return answer