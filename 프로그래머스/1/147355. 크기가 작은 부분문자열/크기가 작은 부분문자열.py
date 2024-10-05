def solution(t, p):
    answer = 0
    start = 0
    end = len(p)
    for i in range(0,len(t)-end+1):
        if int(t[i:i+end]) <= int(p):
            answer+=1
    return answer