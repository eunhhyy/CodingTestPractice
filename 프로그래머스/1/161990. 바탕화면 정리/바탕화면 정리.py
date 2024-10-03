def solution(wallpaper):
    left = []
    right= []
    up = []
    down = []
    for y in range(0,len(wallpaper)):
        for x in range(0,len(wallpaper[0])):   
            if wallpaper[y][x] == "#":
                left.append(y)
                up.append(x)
                right.append(y+1)
                down.append(x+1)
    left.sort()
    right.sort()
    up.sort()
    down.sort()

    return [left[0],up[0],right[-1],down[-1]]