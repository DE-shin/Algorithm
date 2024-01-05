def solution(X, Y):
    answer = ''
    X = list(X); Y = list(Y)
    
    cnt_x = [0] * 10; cnt_y = [0] * 10
    for x in X:
        cnt_x[int(x)] += 1
        
    for y in Y:
        cnt_y[int(y)] += 1
        
    print(cnt_x, cnt_y)
    
    pair = []
    for i, j in zip(cnt_x, cnt_y):
        pair.append(min(i, j))
        
    if sum(pair) == 0:
        answer = "-1"
        
    elif sum(pair[1:]) == 0:
        answer = "0"
        
    else:
        for i in range(1, 11):
            answer += str(10 - i) * pair[-i]
    return answer