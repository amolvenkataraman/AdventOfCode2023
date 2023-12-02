MAX_CUBES = {"red": 12, "green": 13, "blue": 14}

ans = 0

with open("input2.txt", "r") as f:
    for line in f.readlines():
        valid = True
        draws = line.rstrip().split(": ")[1].split("; ")
        for draw in draws:
            cols = [i.split(" ") for i in draw.split(", ")]
            for c in cols:
                if int(c[0]) > MAX_CUBES[c[1]]: valid = False
        
        if valid: ans += int(line.split(": ")[0].split(" ")[1])

print(ans)
