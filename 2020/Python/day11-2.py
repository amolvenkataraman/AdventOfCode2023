import copy

f = open("input11.txt", "r")

layout = [list(i.rstrip()) for i in f]
old_layout = copy.deepcopy(layout)
adj = copy.deepcopy(layout)

h = len(layout)
w = len(layout[0])

f.close()

def get_in_front(coords, direction):
    if direction == "f":
        for i in range(coords[1] + 1, w):
            if old_layout[coords[0]][i] != ".":
                return [coords[0], i]
    
    elif direction == "r":
        for i in range(coords[1] - 1, -1, -1):
            if old_layout[coords[0]][i] != ".":
                return [coords[0], i]

    elif direction == "u":
        for i in range(coords[0] - 1, -1, -1):
            if old_layout[i][coords[1]] != ".":
                return [i, coords[1]]

    elif direction == "d":
        for i in range(coords[0] + 1, h):
            if old_layout[i][coords[1]] != ".":
                return [i, coords[1]]

    elif direction == "tr":
        dist = min(coords[0], w - coords[1] - 1)
        for i in range(dist):
            if old_layout[coords[0] - i][coords[1] + i] != ".":
                return [coords[0] - i, coords[1] + i]

    elif direction == "tl":
        dist = min(coords[0], coords[1])
        for i in range(dist):
            if old_layout[coords[0] - i][coords[1] - i] != ".":
                return [coords[0] - i, coords[1] - i]

    elif direction == "br":
        dist = min(h - coords[0] - 1, w - coords[1] - 1)
        for i in range(dist):
            if old_layout[coords[0] + i][coords[1] + i] != ".":
                return [coords[0] + i, coords[1] + i]

    elif direction == "bl":
        dist = min(h - coords[0] - 1, coords[1])
        for i in range(dist):
            if old_layout[coords[0] + i][coords[1] - i] != ".":
                return [coords[0] + i, coords[1] - i]

    

    

def get_adjacent(coords):
    ans = []

    ans.append(get_in_front(coords, "f"))
    ans.append(get_in_front(coords, "r"))
    ans.append(get_in_front(coords, "u"))
    ans.append(get_in_front(coords, "d"))
    ans.append(get_in_front(coords, "tr"))
    ans.append(get_in_front(coords, "tl"))
    ans.append(get_in_front(coords, "br"))
    ans.append(get_in_front(coords, "bl"))

    ans1 = []
    for i in ans:
        if i != None:
            ans1.append(i)
    
    return ans1

def get_occupied(seats):
    ans = 0
    for i in seats:
        if i != None:
            if old_layout[i[0]][i[1]] == "#":
                ans += 1
    return ans

for i in range(h):
    for j in range(w):
        adj[i][j] = get_adjacent([i, j])

print(adj)

a = 0
while True:
    print(a)
    a += 1
    old_layout = copy.deepcopy(layout)
    for row in range(len(old_layout)):
        for cell in range(len(old_layout[row])):
            if old_layout[row][cell] != ".":
                occupied = get_occupied(adj[row][cell])
                if old_layout[row][cell] == "L" and occupied == 0:
                    layout[row][cell] = "#"
                elif old_layout[row][cell] == "#" and occupied >= 5:
                    layout[row][cell] = "L"
    
    if layout == old_layout:
        break

ans = 0
for i in layout:
    for j in i:
        if j == "#":
            ans += 1
        
print(ans)