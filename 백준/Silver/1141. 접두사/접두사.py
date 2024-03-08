import sys
input = sys.stdin.readline

n = int(input())
arr = set(input().strip() for _ in range(n))
answer = 0

for x in arr:
    cnt = 0
    for y in arr:
        same = True
        
        if len(x) > len(y):
            continue
        else:
            for i in range(len(x)):
                if x[i] != y[i]:
                    same = False
                    break
            if same:
                cnt += 1
    if cnt == 1:
        answer += 1

print(answer)
