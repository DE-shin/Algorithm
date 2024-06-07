def n_formation(n, number):
    table = [str(x) for x in range(10)] + ["A", "B", "C", "D", "E", "F"]
    result = ""
    while number >= n:
        result = table[number % n] + result
        number //= n
    result = table[number] + result
    return result

def solution(n, t, m, p):
    answer = ''
    temp = ''
    i = 0
    while len(temp) <= m*t:
        temp += n_formation(n, i)
        i += 1
    for j in range(t):
        answer += temp[m*j + p -1]

    return answer