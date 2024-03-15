import sys
input = sys.stdin.readline

n =int(input())
arr = list(map(int, input().split()))

table = [0] * n
table[0] = arr[0]

for i in range(1, n):
    table[i] = max(arr[i], arr[i] + table[i-1])

print(max(table))