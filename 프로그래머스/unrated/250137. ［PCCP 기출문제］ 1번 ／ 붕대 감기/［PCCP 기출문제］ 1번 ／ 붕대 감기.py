def solution(bandage, health, attacks):
    answer = 0
    t, x, y = bandage
    seq = 0
    max_health = health
    attack_time = []
    attack_damage = []
    
    def max_hp(hp):
        if hp >= max_health:
            return max_health
        else:
            return hp
    
    for a in attacks:
        attack_time.append(a[0])
        attack_damage.append(a[1])
    
    for time in range(1, attacks[-1][0] + 1):
         
        if time in attack_time:
            seq = 0
            health -= attack_damage[attack_time.index(time)]
            
            if health <= 0:
                return -1
            
        else:
            health = max_hp(health + x)
            seq += 1
        
            if seq == t:
                health = max_hp(health + y)
                seq = 0
        
    
    return health