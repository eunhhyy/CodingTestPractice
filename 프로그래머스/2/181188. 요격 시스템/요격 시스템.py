def solution(targets):
    targets.sort(key= lambda x : x[1])
    shoot = -1
    answer = 0
    for target in targets:
        if target[0] > shoot:
            answer +=1
            shoot = target[1] - 0.5

    return answer