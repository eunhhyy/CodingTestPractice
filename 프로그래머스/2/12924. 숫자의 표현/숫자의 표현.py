def solution(n):
    answer = 1
    for i in range(1,n//2+1):
        tmp = 0
        for j in range(i,n+1):
            tmp += j
            if tmp == n:
                answer +=1
            elif tmp > n:
                break
    return answer