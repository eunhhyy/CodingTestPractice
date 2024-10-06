def make_list(num):
    return_list = []
    for i in range(1,int(num**(1/2))+1):
        if num%i == 0:
            return_list.append((num//i,i))
            i+=1
    return return_list

def solution(brown, yellow):
    mk_list = make_list(brown+yellow)
    for n ,m in mk_list:
        if (brown == 2*n + 2*m -4) and (yellow == n*m -2*n -2*m +4):
            return [n,m]