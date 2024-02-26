import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (y*100) // x
start = 1
end = x
answer = 0
while start <= end:
    mid = (start + end) // 2

    new_z = ((y+mid) * 100) // (x+mid)

    if new_z > z:
        answer = mid
        end = mid - 1

    elif new_z <= z:
        start = mid + 1


if z >= 99:
    print(-1)
else:
    print(answer)