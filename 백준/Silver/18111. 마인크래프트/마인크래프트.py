n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
ans = 10**15; h = 0

land_max = max(max(land))
land_min = min(min(land))

for target in range(land_min, land_max + 1):
    total = 0
    work = 0
    for y in range(n):
        for x in range(m):
            diff = land[y][x] - target
            work += 2*diff if diff >=0 else (-1)*diff
            total += diff


    if total + b >= 0:
        if work <= ans:
            ans = work
            h = max(h, target)


print(ans, h)

    
        
    




