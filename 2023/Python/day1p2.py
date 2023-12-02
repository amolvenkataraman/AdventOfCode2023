ans = 0 # Answer

# Open input file ans iterate through lines
with open("input1.txt", "r") as f:
    for line in f.readlines():
        # Remove trailing newline and replace digit names with their values
        line = line.rstrip() \
        .replace("one", "o1e") \
        .replace("two", "t2o") \
        .replace("three", "th3ee") \
        .replace("four", "fo4r") \
        .replace("five", "fi5e") \
        .replace("six", "s6x") \
        .replace("seven", "se7en") \
        .replace("eight", "ei8ht") \
        .replace("nine", "ni9e")
        # Replace middle character in case of something like "twone", where "two" should be read first
        first = 0; last = 0 # First and last digits
        fdigit = True # Is it the first digit
        for c in line: # Iterate through the characters in the line
            if c.isnumeric(): # If the character is a digit
                if fdigit: first = int(c) # Update first if it is the first digit
                last = int(c) # Always update last
                fdigit = False # No longer the first digit
        ans += ((10 * first) + last) # Update the final answer

print(ans) # Print out the final answer
