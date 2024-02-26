def solution(elements):
    answer = 0
    arr = elements + elements
    
    s = set()
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            t = sum(arr[j:j+i])
            s.add(t)
    answer = len(s)
    return answer