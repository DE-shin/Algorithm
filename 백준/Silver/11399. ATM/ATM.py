from itertools import accumulate
import sys
input = sys.stdin.readline

n = int(input())
print(sum(list(accumulate(sorted(list(map(int, input().split())))))))