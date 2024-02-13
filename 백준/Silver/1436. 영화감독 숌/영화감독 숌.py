import sys
input = sys.stdin.readline

n = int(input())
start = 666
cnt = 0

while True:
    if "666" in str(start):
        cnt += 1
    if n == cnt:
        print(start)
        break
    start += 1

