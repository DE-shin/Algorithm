def solution(prices):
    n = len(prices)
    answer = [x for x in range(n-1, -1, -1)]
    arr = []
    
    for i in range(n):
        while arr and prices[arr[-1]] > prices[i]:
            t = arr.pop()
            answer[t] = i - t
        
        arr.append(i)
    return answer