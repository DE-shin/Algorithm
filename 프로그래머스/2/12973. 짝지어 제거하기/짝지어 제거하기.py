
def solution(s):
    answer = 0

    stack = []
    
    for x in s:
        if len(stack) == 0:
            stack.append(x)
            
        elif stack[-1] == x:
            stack.pop()
            
        else:
            stack.append(x)
    
    if len(stack) == 0:
        answer = 1
            
    return answer