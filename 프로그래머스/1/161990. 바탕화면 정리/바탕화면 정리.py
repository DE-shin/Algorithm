def solution(wallpaper):
    answer = []
    min_y = min_x = 50
    max_y = max_x = 0
    
    for y, row in enumerate(wallpaper):
        if row.find("#") != -1:
            min_x = min(min_x, row.find("#"))
            max_x = max(max_x, row.rfind("#"))
        
            min_y = min(min_y, y)
            max_y = max(max_y, y)
    answer = [min_y, min_x, max_y + 1, max_x + 1] 
    return answer