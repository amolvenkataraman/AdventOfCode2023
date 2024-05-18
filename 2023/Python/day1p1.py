ans = 0 # Answer

# Open input file ans iterate through lines
with open("input1.txt", "r") as f:
    for line in f.readlines():
        # Get all th digits from the string
        digits = [int(i) for i in line if i.isnumeric()]
        ans += ((10 * digits[0]) + digits[-1]) # Update the final answer

print(ans) # Print out the final answer
