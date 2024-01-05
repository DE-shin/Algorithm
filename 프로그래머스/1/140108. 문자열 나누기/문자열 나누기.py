def solution(s):
    answer = 0
    i = 0; j = 0
    cnt_x = 0; cnt_y = 0
    
    while j < len(s):

        x = s[i]
        
        if x == s[j]:
            cnt_x += 1
        else:
            cnt_y += 1
            
        if cnt_x == cnt_y:
            answer += 1
            cnt_x = 0
            cnt_y = 0
            i = j + 1
            j = i
        else:
            j += 1
    if i != j:
        answer += 1
    return answer