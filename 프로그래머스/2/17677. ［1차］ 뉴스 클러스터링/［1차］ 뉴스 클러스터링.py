import math
from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    u1 = []
    u2 = []
    
    for i in range(len(str1) - 1):
        if (str1[i] + str1[i+1]).isalpha():
            u1.append(str1[i] + str1[i+1])
            
    for i in range(len(str2) - 1):
        if (str2[i] + str2[i+1]).isalpha():
            u2.append(str2[i] + str2[i+1])   
            
    c1 = Counter(u1)
    c2 = Counter(u2)
    
    j1 = 0
    j2 = 0
    
    for k, v in c1.items():
        if k in c2:
            j1 += min(c1[k], c2[k])
            j2 += max(c1[k], c2[k])
        else:
            j2 += v
            
    for k, v in c2.items():
        if k not in c1:
            j2 += v
            
    if len(u1) == 0 and len(u2) == 0:
        answer = 1 * 65536
    else:
        answer = int((j1/j2) * 65536)

    return answer