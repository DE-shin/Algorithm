def solution(arr1, arr2):
    
    row_1 = len(arr1)
    col_1 = len(arr1[0])
    row_2 = len(arr2)
    col_2 = len(arr2[0])
    answer = [[0] * col_2 for _ in range(row_1)]
    
    for y1 in range(row_1):
        for x2 in range(col_2):
            for i in range(row_2):
                answer[y1][x2] += arr1[y1][i] * arr2[i][x2]
    
    return answer