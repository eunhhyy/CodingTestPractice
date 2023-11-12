def solution(n):
    if n <= 1:
        return n
    
    answer = 1 + n
    i = 2
    while i*i < n:
        if n%i == 0:
            answer += i
            answer += (n//i)
        i+=1
        
    if i*i == n:
        answer += i
        
    return answer