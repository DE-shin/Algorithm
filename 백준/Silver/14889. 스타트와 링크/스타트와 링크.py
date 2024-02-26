from itertools import *
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

member = set(range(n))
INF = int(1e9)
ans = INF

for t in combinations(member, (n//2)):
    start = t
    link = tuple(member-set(start))

    team_start = 0
    team_link = 0

    for x, y in combinations(start, 2):
        team_start += arr[x][y]
        team_start += arr[y][x]
        
    for i, j in combinations(link, 2):
        team_link += arr[i][j]
        team_link += arr[j][i]

    ans = min(ans, abs(team_start - team_link))

print(ans)