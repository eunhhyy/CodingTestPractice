def solution(n, m, section):
    answer = 1
    tmp = section[0]
    for i in section:
        if i > tmp + (m-1):
            tmp = i
            answer+=1
    return answer