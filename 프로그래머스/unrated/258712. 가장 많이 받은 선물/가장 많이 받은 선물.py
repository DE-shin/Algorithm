from itertools import combinations

def solution(friends, gifts):
    answer = [0] * len(friends)
    f_to_n = dict(zip(friends, range(len(friends))))
    
    present = [[0] * len(friends) for _ in range(len(friends))]
    
    for a_to_b in gifts:
        a, b = a_to_b.split()
        
        present[f_to_n[a]][f_to_n[b]] += 1
        
    present_idx = [0] * len(friends)
    
    for name in f_to_n:
        present_receive = 0
        for i in range(len(friends)):
            present_receive += present[i][f_to_n[name]]
        present_give = sum(present[f_to_n[name]])
        
        present_idx[f_to_n[name]] = present_give - present_receive
        
        
    for x, y in combinations(f_to_n, 2):
        x_to_y = present[f_to_n[x]][f_to_n[y]]
        y_to_x = present[f_to_n[y]][f_to_n[x]]
    
        if x_to_y > y_to_x:
            answer[f_to_n[x]] += 1
        elif x_to_y < y_to_x:
            answer[f_to_n[y]] += 1
        else:
            if present_idx[f_to_n[x]] > present_idx[f_to_n[y]]:
                answer[f_to_n[x]] += 1
            elif present_idx[f_to_n[x]] < present_idx[f_to_n[y]]:
                answer[f_to_n[y]] += 1
            else:
                pass
    return max(answer)