import math

ans = 0

with open("input2.txt", "r") as f:
    for line in f.readlines():
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        draws = line.rstrip().split(": ")[1].split("; ")
        for draw in draws:
            cols = [i.split(" ") for i in draw.split(", ")]
            for c in cols:
                min_cubes[c[1]] = max(min_cubes[c[1]], int(c[0]))
        
        ans += math.prod([min_cubes[i] for i in min_cubes])

print(ans)
