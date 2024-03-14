import sys
input = sys.stdin.readline

cnt = 0
n = int(input())

while True:
    if n % 5 == 0:
        cnt += n // 5
        break

    else:
        n -= 3
        cnt += 1

    if n < 0:
        cnt = -1
        break
    if n == 0:
        break

print(cnt)