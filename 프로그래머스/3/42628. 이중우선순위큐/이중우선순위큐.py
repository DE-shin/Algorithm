
def solution(operations):
    answer = [0, 0]
    arr = []
    for oper in operations:
        if arr:
            if oper == "D 1":
                arr.pop()
            elif oper == "D -1":
                arr.pop(0)
        if oper[0] == "I":
            num = int(oper.replace("I", ""))
            arr.append(num)
            arr.sort()
    if arr:
        answer[0] = max(arr)
        answer[1] = min(arr)
    return answer