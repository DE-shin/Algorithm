def solution(board, moves):
    answer = 0
    stack = []

    for c in moves:
        for i in range(len(board)):
            if board[i][c-1]:
                stack.append(board[i][c-1])
                board[i][c-1] = 0
                break
            else:
                pass

        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    return answer