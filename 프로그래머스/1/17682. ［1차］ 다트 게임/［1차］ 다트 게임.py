def solution(dartResult):
    answer = 0
    bonus = {"S" : 1, "D" : 2, "T": 3}
    calc = []
    num = ""
    for letter in dartResult:
        
        if letter.isdecimal():
            num += letter
        else:
            if len(num) > 0:
                calc.append(int(num))
            idx = len(calc) - 1
            num = ""
            if letter in bonus:
                power = bonus[letter]
                calc[idx] = calc[idx] ** power
            elif letter == "*":
                if idx == 0:
                    calc[idx] *= 2
                else:
                    calc[idx] *=2
                    calc[idx-1] *= 2
            elif letter == "#":
                calc[idx] *= -1
    
    return sum(calc)