from collections import deque
def solution(s):
    answer = 0
    
    def chk(letters):
        q = deque()
        left = ["[", "{", "("]
        right = ["]", "}", ")"]
        
        for l in letters:
            if l in left:
                q.append(l)
            else:
                if q:
                    if q.pop() != left[right.index(l)]:
                        return False
                else:
                    return False
        
        return True
        
    if len(s) % 2 != 0:
        answer = 0
    else:
        for _ in range(len(s)):
            s = s[1:] + s[0]
            if chk(s):
                answer += 1
            
    return answer