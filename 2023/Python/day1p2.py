ans = 0 # Answer

# Open input file ans iterate through lines
with open("input1.txt", "r") as f:
    for line in f.readlines():
        # Remove trailing newline and replace digit names with their values
        line = line.rstrip() \
            .replace("one", "o1e").replace("two", "t2o").replace("three", "th3ee") \
            .replace("four", "fo4r").replace("five", "fi5e").replace("six", "s6x") \
            .replace("seven", "se7en").replace("eight", "ei8ht").replace("nine", "ni9e")
        # Replace middle character in case of something like "twone", where "two" should be read first
        # Get all th digits from the string
        digits = [int(i) for i in line if i.isnumeric()]
        ans += ((10 * digits[0]) + digits[-1]) # Update the final answer

print(ans) # Print out the final answer
