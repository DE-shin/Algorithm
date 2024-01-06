def solution(keymap, targets):
    alpha = dict()
    answer = []
    
    for word in keymap:
        for idx, letter in enumerate(word):
            if letter not in alpha:
                alpha[letter] = idx + 1
            else:
                alpha[letter] = min(alpha[letter], idx + 1)
                
    for x in targets:
        print(x)
        ans = 0
        for y in x:
            if y not in alpha:
                ans = -1
                break
            else:
                ans += alpha[y]
        answer.append(ans)
    return answer