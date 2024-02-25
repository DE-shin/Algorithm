import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

h = []
heapq.heappush(h, arr[0][1])

for i in range(1, len(arr)):
    if h[0] <= arr[i][0]:
        heapq.heappop(h)
    heapq.heappush(h, arr[i][1])
    
print(len(h))