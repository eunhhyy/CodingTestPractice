def solution(sizes):
    row = []
    col = []
    for x,y in sizes:
        if x < y:
            row.append(x)
            col.append(y)
        else:
            row.append(y)
            col.append(x)

    return max(row) * max(col)