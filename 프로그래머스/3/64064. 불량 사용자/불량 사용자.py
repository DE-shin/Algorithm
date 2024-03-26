def solution(user_id, banned_id):
    answer = 0
    ans = []
    n = len(user_id)
    m = len(banned_id)
    visited = [False] * n
    filled = [False] * m
    
    def chk(a, b):
        if len(a) != len(b):
            return False
        else:
            for idx in range(len(a)):
                if b[idx] == "*":
                    pass
                elif a[idx] != b[idx]:
                    return False
            return True
    
    def dfs(u, j):
        nonlocal answer, ans
        if sum(filled) == m:
            temp = set()
            for idxx in range(n):
                if visited[idxx]:
                    temp.add(user_id[idxx])
            if temp not in ans:
                ans.append(temp)
            answer += 1
            return

        for i in range(n):
            if not visited[i] and chk(user_id[i], banned_id[j+1]):
                visited[i] = True
                filled[j+1] = True
                dfs(user_id[i], j+1)
                visited[i] = False
                filled[j+1] = False
                
    for i in range(n):
        if chk(user_id[i], banned_id[0]):
            visited[i] = True
            filled[0] = True
            dfs(user_id[i], 0)
            visited[i] = False
            filled[0] = False

    answer = len(ans)
    return answer