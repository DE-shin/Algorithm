import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input()) # start node
graph = [[] for _ in range(v+1)]
for _ in range(e):
    start, end, distance = map(int, input().split())
    graph[start].append((end, distance))


INF = int(1e9)
cost = [INF] * (v+1)

def dij(start_node):
    q = []
    cost[start_node] = 0
    heapq.heappush(q, (0, start_node))

    while q:
        cost_now, node_now = heapq.heappop(q)

        if cost_now > cost[node_now]:
            continue

        for node_nxt, cost_nxt in graph[node_now]:
            t = cost_nxt + cost_now
            if t < cost[node_nxt]:
                cost[node_nxt] = t
                heapq.heappush(q, (t, node_nxt))

dij(k)

for i in range(1, v+1):
    if cost[i] == INF:
        print("INF")
    else:
        print(cost[i])
    