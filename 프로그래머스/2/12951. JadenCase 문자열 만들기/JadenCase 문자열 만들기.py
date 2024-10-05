def solution(s):
    answer = ''
    flag = True
    for i in s:
        if i == " ":
            answer += "*"
            flag = True
        elif i != " "and flag == True:
            answer += i.upper()
            flag = False
        elif i != " " and flag == False:
            answer += i.lower()

    answer = answer.replace("*"," ")
    return answer