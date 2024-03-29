def solution(n, costs):
    answer = 0
    parent = list(range(n))

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
            
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
    arr = sorted(costs, key=lambda x:x[2])
    
    for ar in arr:
        a, b, cost = ar
        if find_parent(parent, a) != find_parent(parent, b):
            union(parent, a, b)
            answer += cost
            print(answer, parent)
    return answer