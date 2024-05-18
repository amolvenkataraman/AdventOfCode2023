import copy

f = open("input11.txt", "r")

layout = [list(i.rstrip()) for i in f]
old_layout = copy.deepcopy(layout)

h = len(layout)
w = len(layout[0])

f.close()

def get_adjacent(coords):
    ans = []

    for i in range(coords[0] - 1, coords[0] + 2):
        for j in range(coords[1] - 1, coords[1] + 2):
            if i != coords[0] or j != coords[1]:
                if i >= 0 and i < h and j >= 0 and j < w:
                    if old_layout[i][j] != ".":
                        ans.append([i, j])
    
    return ans

def get_occupied(seats):
    ans = 0
    for i in seats:
        if old_layout[i[0]][i[1]] == "#":
            ans += 1
    
    return ans

while True:
    old_layout = copy.deepcopy(layout)
    for row in range(len(old_layout)):
        for cell in range(len(old_layout[row])):
            if old_layout[row][cell] != ".":
                occupied = get_occupied(get_adjacent([row, cell]))
                if old_layout[row][cell] == "L" and occupied == 0:
                    layout[row][cell] = "#"
                elif old_layout[row][cell] == "#" and occupied >= 4:
                    layout[row][cell] = "L"
    
    if layout == old_layout:
        break

ans = 0
for i in layout:
    for j in i:
        if j == "#":
            ans += 1
        
print(ans)