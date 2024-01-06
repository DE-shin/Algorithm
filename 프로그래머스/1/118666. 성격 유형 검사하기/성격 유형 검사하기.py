def solution(survey, choices):
    answer = ''
    personality = ["RT", "CF", "JM", "AN"]
    score = [0, 0, 0, 0]
    for p, s in zip(survey, choices):
        if p == "RT":
            score[0] += s - 4
        elif p == "TR":
            score[0] -= s - 4
            
        elif p == "CF":
            score[1] += s - 4
        elif p == "FC":
            score[1] -= s - 4
        
        elif p == "JM":
            score[2] += s - 4
        elif p == "MJ":
            score[2] -= s - 4
            
        elif p == "AN":
            score[3] += s - 4
        else:
            score[3] -= s - 4
            

    for i, s in enumerate(score):
        if s > 0:
            answer += personality[i][1]
        else:
            answer += personality[i][0]
                              
                              
    return answer