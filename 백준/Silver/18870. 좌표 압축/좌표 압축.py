from bisect import *
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = []

arr_sort = (sorted(set(arr)))

for x in arr:
    l = bisect_left(arr_sort, x)
    answer.append(l)

print(*answer)