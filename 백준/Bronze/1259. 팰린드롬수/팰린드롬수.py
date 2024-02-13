import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if int(s) == 0:
        break
    pel = True
    if len(s) % 2 == 0:
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                pel = False
                break
        if pel:
            print("yes")
        else:
            print("no")
    else:
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                pel = False
                break
        if pel:
            print("yes")
        else:
            print("no")
