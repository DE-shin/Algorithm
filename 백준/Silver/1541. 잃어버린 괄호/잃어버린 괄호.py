import sys
input = sys.stdin.readline

arr = input().strip()

number = ""
sub = False
answer = 0
for x in arr:
    
    if x.isdecimal():
        number += x
    else:
        if not sub:
            answer += int(number)
            number = ""
        if sub:
            answer -= int(number)
            number = ""

    if x == '-':
        sub = True

if sub:
    answer -= int(number)
else:
    answer += int(number)

print(answer)
    