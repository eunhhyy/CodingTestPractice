def solution(n):
    i = n**(1/2)
    if i%1 == 0:
        return (int(i)+1)**2 
    return -1