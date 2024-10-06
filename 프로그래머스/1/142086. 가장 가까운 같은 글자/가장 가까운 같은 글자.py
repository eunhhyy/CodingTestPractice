def solution(s):
    word = {item :-10 for item in s}
    result =[]
    for idx, i in enumerate(s):
        if word[i] == -10:
            word[i] = idx
            result.append(-1)
        else:
            result.append(idx - word[i])
            word[i] = idx
    return result