import sys
from itertools import *
input = sys.stdin.readline

answer = "NO"
n = int(input())
graph = [list(input().split()) for _ in range(n)]
available = []
teacher = []
for y in range(n):
    for x in range(n):
        if graph[y][x] == "X":
            available.append([y, x])
        elif graph[y][x] == "T":
            teacher.append([y, x])
t = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def isinside(y, x):
    return 0 <= y < n and 0 <= x < n

def dfs(y, x):
    
    nostudent = True
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        while isinside(ny, nx):
        
            if graph[ny][nx] == "S":
                nostudent = False
                return nostudent
            
            elif graph[ny][nx] == "X" or graph[ny][nx] == "T":
                ny += dy[i]
                nx += dx[i]
            
            else:
                break
            
    return nostudent

for walls in combinations(available, 3):
    # make walls
    for y, x in walls:
        graph[y][x] = "O"
        
    t = 0    
    # for each teacher
    for ty, tx in teacher:
        if dfs(ty, tx) == True:
            t += 1
        else:
            t = 0
    
    if t == len(teacher):
        answer = "YES"
        break
        
    # clear walls
    for y, x in walls:
        graph[y][x] = "X"


print(answer)