def solution(babbling):
    answer = 0
    speak = {"aya" : "0", "ye" : "1", "woo" : "2", "ma" : "3"}
    can_speak = ["0", "1", "2", "3"]
    for x in babbling:
        temp = x
        
        for y in speak:
            temp = temp.replace(y, speak[y], 30)
        
        temp = list(temp)
        able = True
        for i, j in enumerate(temp):
            if i < len(temp)-1:
                if (j not in can_speak) or (temp[i] == temp[i+1]):
                    able = False
                    break
            elif i == len(temp)-1:
                if j not in can_speak:
                    able = False
                    break
        if able:
            answer += 1
    return answer