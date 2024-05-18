import math

f = open("input12.txt", "r")

directions = [[i.rstrip()[:1], int(i.rstrip()[1:])] for i in f]

f.close()

ship = [0, 0]
waypoint = [10, -1]

ccw_rotate = {90: lambda x, y: (y, -x),
              180: lambda x, y: (-x, -y),
              270: lambda x, y: (-y, x)}

cw_rotate = {90: lambda x, y: (-y, x),
             180: lambda x, y: (-x, -y),
             270: lambda x, y: (y, -x)}

for i in directions:
    if i[0] == 'N':
        waypoint[1] -= i[1]
    elif i[0] == 'S':
        waypoint[1] += i[1]
    elif i[0] == 'E':
        waypoint[0] += i[1]
    elif i[0] == 'W':
        waypoint[0] -= i[1]
    
    elif i[0] == 'F':
        temp = [(waypoint[0] - ship[0]), (waypoint[1] - ship[1])]
        ship[0] = (temp[0]) * i[1]
        ship[1] = (temp[1]) * i[1]

        waypoint[0] = (ship[0] + temp[0])
        waypoint[1] = (ship[1] + temp[1])

    else:
        if i[0] == 'L':
            waypoint[0], waypoint[1] = ccw_rotate.get(i[1])(waypoint[0] - ship[0], waypoint[1] - ship[1])
            waypoint[0] += ship[0]
            waypoint[1] += ship[1]
        elif i[0] == 'R':
            waypoint[0], waypoint[1] = cw_rotate.get(i[1])(waypoint[0] - ship[0], waypoint[1] - ship[1])
            waypoint[0] += ship[0]
            waypoint[1] += ship[1]

print(abs(ship[0]) + abs(ship[1]))