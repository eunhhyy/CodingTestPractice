def to_ten(n : str):
    result = 0
    idx = 0
    for i in n[::-1]:
        result += (2**idx*int(i))
        idx+=1
    return result
    
def solution(n):
    i = 1
    while True:
        origin = bin(n)[2:]
        nx = bin(n+i)[2:]
        origin_len = len(origin.replace('0',''))
        nx_len = len(nx.replace('0',''))
        if origin_len == nx_len:
            return to_ten(nx)
        i+=1