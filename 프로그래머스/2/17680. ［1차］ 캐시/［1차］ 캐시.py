def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if cacheSize > 0:
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
                
            else:
                if len(cache) < cacheSize:
                    cache.append(city)
                else:
                    cache.pop(0)
                    cache.append(city)
                answer += 5

        else:
            answer += 5
    
    return answer