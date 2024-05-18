f = open("input3.txt", "r")

map_ = [i.rstrip() for i in f]

f.close()

v_pos = 0
h_pos = 0

ans = 0
while True:
    h_pos += 3
    v_pos += 1

    if map_[v_pos][h_pos % len(map_[0])] == "#":
        ans += 1

    if v_pos >= len(map_) - 1:
        break

print(ans)