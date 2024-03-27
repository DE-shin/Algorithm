from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for y, x in edge:
        graph[y].append(x)
        graph[x].append(y)
        
    def bfs(s):
        cnt = 0
        min_v = 0
        visited = [False] * (n+1)
        q = deque()
        visited[s] = True
        q.append((0, s))

        while q:
            cost, start = q.popleft()
            
            if cost == min_v:
                cnt += 1
            elif cost > min_v:
                min_v = cost
                cnt = 1

            for nend in graph[start]:
                if not visited[nend]:
                    visited[nend] = True
                    q.append((cost+1, nend))
        return cnt
    answer = bfs(1)
    return answer