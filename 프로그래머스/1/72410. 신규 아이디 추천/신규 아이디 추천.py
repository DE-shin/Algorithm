def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    new_id2 = ''
    
    for x in new_id:
        if x.isalnum() or x in ['-', '_', '.']:
            new_id2 += x
    
    while new_id2.find("..") != -1:
        new_id2 = new_id2.replace("..", '.')
    
    new_id2 = new_id2.strip(".")
    
    if new_id2 == "":
        new_id2 += "a"
        
    if len(new_id2) >= 16:
        new_id2 = new_id2[:15]
    
    new_id2 = new_id2.strip(".")
    
    if len(new_id2) <= 2:
        while len(new_id2) < 3:
            new_id2 += new_id2[-1]
        
    answer = new_id2
    
    return answer