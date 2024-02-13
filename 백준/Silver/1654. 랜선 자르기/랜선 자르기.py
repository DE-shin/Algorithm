import sys
input = sys.stdin.readline

k, n = map(int, input().split())
wires = []
for _ in range(k):
    wires.append(int(input()))
start = 1
end = max(wires)
mid = (start + end) // 2

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for wire in wires:
        cnt += (wire // mid)


    if cnt < n:
        end = mid - 1
        
    elif cnt >= n:
        start = mid + 1


print(end)