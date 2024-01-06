def solution(park, routes):
    
    def is_available(y, x):
        return 0 <= y < len(park) and 0 <= x < len(park[0])
    
    def is_obstruct(y, x, dy, dx):
        if dx == 0:
            if dy > 0 :
                for i in range(1, dy+1):
                    if park[y+i][x] == "X":
                        return False
            else:
                for i in range(-1, dy-1, -1):
                    if park[y+i][x] == "X":
                        return False
        else:
            if dx > 0:
                for i in range(1, dx+1):
                    if park[y][x+i] == "X":
                        return False
            else:
                for i in range(-1, dx-1, -1):
                    if park[y][x+i] == "X":
                        return False  
        return True
    
    unit_direction = {"N" : (-1, 0), "S" : (1, 0), "W" : (0, -1), "E" : (0, 1)}
    
    for i, row in enumerate(park):
        if "S" in row:
            y = i
            x = row.index("S")
            break
            
    for route in routes:
        direction, distance = route.split()
        dy = unit_direction[direction][0] * int(distance)
        dx = unit_direction[direction][1] * int(distance)
        ny = y + dy
        nx = x + dx
        
        if is_available(ny, nx) and is_obstruct(y, x, dy, dx):
            y = ny
            x = nx
    
    return [y, x]