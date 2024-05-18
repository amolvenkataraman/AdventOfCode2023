import math

f = open("input12.txt", "r")

directions = [[i.rstrip()[:1], int(i.rstrip()[1:])] for i in f]

f.close()

pos1 = [0, 0]
pos2 = [0, 0]
angle = 0

for i in directions:
    if i[0] == 'N':
        pos1[1] -= i[1]
    elif i[0] == 'S':
        pos1[1] += i[1]
    elif i[0] == 'E':
        pos1[0] += i[1]
    elif i[0] == 'W':
        pos1[0] -= i[1]

    elif i[0] == 'L':
        angle -= i[1]
    elif i[0] == 'R':
        angle += i[1]

    elif i[0] == 'F':
        pos2[1] += math.sin(math.radians(angle)) * i[1]
        pos2[0] += math.cos(math.radians(angle)) * i[1]

print((abs(pos1[0]) + abs(pos1[1]) + abs(pos2[0]) + abs(pos2[1])))