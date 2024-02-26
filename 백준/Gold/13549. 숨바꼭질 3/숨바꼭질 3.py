from collections import deque
import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * (100_001)

q = []
heapq.heappush(q, (0, n))
visited[n] = True

while q:
    cost_now, loc_now = heapq.heappop(q)

    if loc_now == k:
        print(cost_now)
        break

    for i in range(3):
        if i == 0:
            loc_nxt = loc_now * 2
            cost_nxt = cost_now
        elif i == 1:
            loc_nxt = loc_now + 1
            cost_nxt = cost_now + 1
        else:
            loc_nxt = loc_now - 1
            cost_nxt = cost_now + 1

        if 0 <= loc_nxt <= 100000 and not visited[loc_nxt]:
            heapq.heappush(q, (cost_nxt, loc_nxt))
            visited[loc_nxt] = True