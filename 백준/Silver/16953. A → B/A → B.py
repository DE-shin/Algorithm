import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 0
okay = True

while True:
    if str(b)[-1] == "1":
        b = int(str(b)[:-1])

    elif b % 2 == 0:
        b = b // 2

    else:
        okay = False
        break

    cnt += 1
    
    if a == b:
        break

    if a > b:
        okay = False
        break

if okay:
    print(cnt + 1)
else:
    print(-1)