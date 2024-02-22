import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    arr.sort(key=lambda x: x[0])

    cnt = 1
    max_value = arr[0][1]

    for i in range(1, n):
        if arr[i][1] < max_value:
            cnt += 1
            max_value = arr[i][1]

    print(cnt)