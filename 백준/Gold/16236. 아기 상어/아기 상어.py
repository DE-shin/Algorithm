import sys
import heapq
from collections import deque
input = sys.stdin.readline

# Initial Settings
n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
answer = 0
shark_size = 2
now_eat = 0
for y in range(n):
    for x in range(n):
        if space[y][x] == 9:
            shark_pos = (y, x)
            break

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# Check_Inside
def chk_inside(y, x):
    return 0 <= y < n and 0 <= x < n

# Bfs
def bfs(y, x):
    # bfs initial
    global shark_size, shark_pos, now_eat, space, answer
    visited = [[False] * n for _ in range(n)]
    q = deque()
    eat = []
    
    visited[y][x] = True
    q.append((0, space[y][x], y, x))

    # bfs main
    while q:
        dis, fish_size, now_y, now_x = q.popleft()
      
        # chk for eat
        if 1 <= fish_size < shark_size and fish_size <= 6:
            heapq.heappush(eat, (dis, now_y, now_x))

        if len(eat) >= shark_size:
            break

        for i in range(4):
            nxt_y = now_y + dy[i]
            nxt_x = now_x + dx[i]

            if chk_inside(nxt_y, nxt_x) and not visited[nxt_y][nxt_x]:
                f = space[nxt_y][nxt_x]
                if f <= shark_size and f <= 6:
                    visited[nxt_y][nxt_x] = True
                    q.append((dis + 1, f, nxt_y, nxt_x))
                
        

    # after bfs
    if len(eat) == 0:
        return -1
        
    else:
        eat_dis, eat_y, eat_x = heapq.heappop(eat)
        
        now_eat += 1
        shark_pos = (eat_y, eat_x)

        answer += eat_dis

        # move shark_size
        space[y][x] = 0
        space[eat_y][eat_x] = 9

        if now_eat == shark_size:
            shark_size += 1
            now_eat = 0
            
        return 1

# Main

while bfs(shark_pos[0], shark_pos[1]) == 1:
    pass

print(answer)