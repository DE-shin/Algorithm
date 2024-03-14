import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ps = input().strip()
    n = int(input())
    if n > 0:
        arr = list(map(int, input().strip().strip("[]").split(",")))
    else:
        temp = input()
        arr = []
    cnt = 0
    initial = 1
    
    for p in ps:
        if p == 'D':
            if len(arr) == 0:
                cnt = -1
                break
            elif initial:
                arr.pop(0)
            elif not initial:
                arr.pop()


        if p == 'R':
            initial = 1 - initial
            cnt += 1

    if cnt == -1:
        print("error")
    else:
        if cnt % 2 == 1:
            arr.reverse()

        print("[" + ",".join(map(str, arr)) + "]")