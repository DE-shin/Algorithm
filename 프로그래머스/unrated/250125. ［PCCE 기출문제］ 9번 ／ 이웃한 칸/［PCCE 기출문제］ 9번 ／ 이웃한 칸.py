def solution(board, h, w):
    answer = 0
    n = len(board)
    
    def is_available(y, x):
        return 0 <= y < n and 0<= x < n
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    now = board[h][w]
    for i in range(4):
        nh = h + dy[i]
        nw = w + dx[i]
        
        if is_available(nh, nw) and now == board[nh][nw]:
            answer += 1
            
    
    return answer