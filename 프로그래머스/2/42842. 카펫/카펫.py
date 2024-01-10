def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i == 0:
            x = i
            y  = yellow // i
            
            if brown + yellow == (x+2)*(y+2) :
                answer = [y+2, x+2]
    return answer