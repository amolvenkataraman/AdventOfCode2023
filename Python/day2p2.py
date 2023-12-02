import math

ans = 0 # Answer

# Open file and iterate through the lines
with open("input2.txt", "r") as f:
    for line in f.readlines():
        # Minimum number of cubes of each type for the game
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        draws = line.rstrip().split(": ")[1].split("; ") # Get each individual set of draws
        for draw in draws:
            # Get the number of cubes of each colour and update min_cubes if needed
            cols = [i.split(" ") for i in draw.split(", ")]
            for c in cols:
                min_cubes[c[1]] = max(min_cubes[c[1]], int(c[0]))
        
        ans += math.prod([min_cubes[i] for i in min_cubes]) # Update the final answer

print(ans)
