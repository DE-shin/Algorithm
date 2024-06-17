
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    arr = []
    
    for i in range(n):
        while arr and numbers[arr[-1]] < numbers[i]:
            answer[arr.pop()] = numbers[i]
        
        arr.append(i)
    
    return answer