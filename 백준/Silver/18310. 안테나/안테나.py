import sys
input = sys.stdin.readline

n = int(input())
house = list(map(int, input().split()))
house.sort()
i = 0
j = len(house) - 1
mid = (i + j) // 2

def total_distance(n):
    sum = 0
    for h in house:
        sum += abs(h-n)
    return sum

while i != j:
    l = total_distance(house[i])
    r = total_distance(house[j])
    m = total_distance(house[mid])

    if l > m:
        i = mid
        mid = (i + j) // 2
    elif r < m:
        j = mid
        mid = (i + j) // 2
    else:
        j = mid
        mid = (i + j) // 2

print(house[i])