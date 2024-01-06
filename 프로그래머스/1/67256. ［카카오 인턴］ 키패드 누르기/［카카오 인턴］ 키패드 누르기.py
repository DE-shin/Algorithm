def solution(numbers, hand):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 0, 11]]
    key_l = [1, 4, 7]
    key_r = [3, 6, 9]
    idx_yl = 3
    idx_xl = 0
    idx_yr = 3
    idx_xr = 2
    answer = ''
    
    def get_loc(num):
        for j, row in enumerate(keypad):
            if num in row:
                y = j
                x = row.index(num)
        return y, x
    
    def distance(l, r, n):
        dl = abs(l[0] - n[0]) + abs(l[1] - n[1])
        dr = abs(r[0] - n[0]) + abs(r[1] - n[1])
        if dl > dr:
            return -1
        elif dl < dr:
            return 1
        else:
            return 0
    
    for n in numbers:
        if n in key_l:
            answer += "L"
            idx_yl, idx_xl = get_loc(n)
        elif n in key_r:
            answer += "R"
            idx_yr, idx_xr = get_loc(n)
        else:
            d = distance((idx_yl, idx_xl), (idx_yr, idx_xr), get_loc(n))
            if d == 1:
                answer += "L"
                idx_yl, idx_xl = get_loc(n)
            elif d == -1:
                answer += "R"
                idx_yr, idx_xr = get_loc(n)
                
            else:
                if hand == "left":
                    answer += "L"
                    idx_yl, idx_xl = get_loc(n)
                else:
                    answer += "R"
                    idx_yr, idx_xr = get_loc(n)
    return answer