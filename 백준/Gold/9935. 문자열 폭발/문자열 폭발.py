import sys
input = sys.stdin.readline

arr = input().strip()
bomb = input().strip()
b = len(bomb)
answer = []
for x in arr:
    answer.append(x)

    if answer[-b:] == list(bomb):
        for _ in range(b):
            answer.pop()

if answer:
    print("".join(answer))
else:
    print("FRULA")