def solution(n):
    array = list(str(n))
    return list(int(i) for i in array[::-1])