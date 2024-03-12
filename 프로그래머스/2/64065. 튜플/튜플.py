def solution(s):
    answer = []
    s = s[1:-1]
    arr = []
    tup = []
    for l in s:
        if l == "{":
            temp = ""
        elif l == "}":
            arr.append(temp)
        else:
            temp += l
    for x in arr:
        tup.append(list(map(int, x.split(","))))
    tup.sort(key = lambda x:len(x))
    for t in tup:
        for tt in t:
            if tt not in answer:
                answer.append(tt)
    
    return answer