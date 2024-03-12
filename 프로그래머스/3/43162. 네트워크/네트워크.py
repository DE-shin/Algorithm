def solution(n, computers):
    answer = 0
    visited = [False] * n
        
    def dfs(y):
        visited[y] = True
        
        for x in range(n):
            if computers[y][x] and not visited[x]:
                dfs(x)
        return
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
        
    return answer