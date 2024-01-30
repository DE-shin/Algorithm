from collections import deque
import sys
input = sys.stdin.readline

# inputs
n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
dir = [list(map(str, input().split())) for _ in range(l)]

# Initial Setting
answer = 0
b = [[0] * n for _ in range(n)]
for ay, ax in apple:
    b[ay-1][ax-1] = 1 # Apple
q = deque()

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
i = 0

# Functions
def check_inside(y, x):
    return 0 <= y < n and 0 <= x < n

def check_mybody(y, x):
    if (y, x) in q:
        return True
    else:
        return False

y = 0; x = 0
q.append((y, x))
dir_idx = 0

while True:

    answer += 1
    ny = y + dy[i]
    nx = x + dx[i]

    if check_inside(ny, nx) and not check_mybody(ny, nx): # move
        q.append((ny, nx))
        if b[ny][nx] != 1: # not apple -> pop
            q.popleft()
        else:
            b[ny][nx] = 0
        y = ny
        x = nx
    else: # game over
        break

    # direction 
    if dir_idx < l and int(dir[dir_idx][0]) == answer:
        if dir[dir_idx][1] == 'L':
            if i == 0:
                i = 3
            else:
                i -= 1
        else:
            if i == 3:
                i = 0
            else:
                i += 1

        dir_idx += 1
        
    

print(answer)
    
    