def solution(m, n, puddles):
    answer = 0
    divider = 1000000007
    
    graph = [[-1] * m for _ in range(n)]
    if len(puddles[0]) > 0:
        for mm, nn in puddles:
            graph[nn-1][mm-1] = -2
        
    dy = [1, 0]
    dx = [0, 1]
    
    def chk(y, x):
        return 0 <= y < n and 0 <= x < m
    
    def dfs(y, x):
        if y == n-1 and x == m-1:
            return 1
        
        if graph[y][x] == -1:
            graph[y][x] = 0
            
            for i in range(2):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if chk(ny, nx) and graph[ny][nx] > -2:
                    graph[y][x] += dfs(ny, nx) 
                    
        return graph[y][x]
    
    dfs(0, 0)
    answer = graph[0][0] % divider
    return answer