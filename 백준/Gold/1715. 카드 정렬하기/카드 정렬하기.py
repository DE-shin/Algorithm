import heapq

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

answer = 0

while len(heap) != 1:
    n1 = heapq.heappop(heap)
    n2 = heapq.heappop(heap)

    temp = n1 + n2
    answer += temp
    heapq.heappush(heap, temp)

print(answer)