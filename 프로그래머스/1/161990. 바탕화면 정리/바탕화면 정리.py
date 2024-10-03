def solution(wallpaper):
    left = []
    up = []
    for y in range(0,len(wallpaper)):
        for x in range(0,len(wallpaper[0])):   
            if wallpaper[y][x] == "#":
                left.append(y)
                up.append(x)

    left.sort()
    up.sort()

    return [left[0],up[0],left[-1]+1,up[-1]+1]