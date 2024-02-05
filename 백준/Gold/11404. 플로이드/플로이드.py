import sys
input = sys.stdin.readline

INF = int(1e7)
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    if cost < graph[start][end]:
        graph[start][end] = cost

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
        