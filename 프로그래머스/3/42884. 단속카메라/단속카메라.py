def solution(routes):
    answer = -50000
    camera = 0
    routes.sort(key = lambda x : x[1])
    for route in routes:
        if route[0] > answer:
            camera+=1
            answer = route[1]
    return camera