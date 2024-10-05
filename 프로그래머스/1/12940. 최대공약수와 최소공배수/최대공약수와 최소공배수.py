def solution(n, m):
    answer = []
    def first(n,m):
        num = 0
        for i in range(1,n+1):
            if n%i == 0 and m%i ==0:
                num = i
        return num
    num = first(n,m)
    max_num = (n/num)*(m/num)*num
    return [num, max_num]