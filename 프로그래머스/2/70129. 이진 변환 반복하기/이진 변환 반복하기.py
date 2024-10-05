def remove_zero(s:str):
    d = len(s)
    s = s.replace("0","")
    sd = d - len(s)
    return sd, s

def dec(s):
    num = len(s)
    return format(num,'b')
        
def solution(s):
    cnt_0 = 0
    cnt_num = 0
    while s != "1":
        sd, s = remove_zero(s)
        cnt_0 += sd
        s = dec(s)
        cnt_num+=1
    
    return [cnt_num, cnt_0]