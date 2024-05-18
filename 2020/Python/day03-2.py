f = open("input3.txt", "r")

map_ = [i.rstrip() for i in f]

f.close()


moves = [1, 1], [3, 1], [5, 1], [7, 1], [1, 2]
finalans = 1
for i in moves:
    v_pos = 0
    h_pos = 0
    ans = 0
    while True:
        h_pos += i[0]
        v_pos += i[1]

        if map_[v_pos][h_pos % len(map_[0])] == "#":
            ans += 1

        if v_pos >= len(map_) - 1:
            break
    finalans *= ans

print(finalans)