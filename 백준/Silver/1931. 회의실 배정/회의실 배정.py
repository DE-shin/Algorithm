import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    t_start, t_end = map(int, input().split())
    arr.append((t_start, t_end))

arr.sort(key = lambda x: (x[1], x[0]))
cnt = 0
end = 0
for i in range(n):
    if arr[i][0] >= end:
        cnt += 1
        end = arr[i][1]

print(cnt)