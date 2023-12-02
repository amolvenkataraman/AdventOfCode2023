ans = 0 # Answer

# Open input file ans iterate through lines
with open("input1.txt", "r") as f:
    for line in f.readlines():
        first = 0; last = 0 # First and last digits
        fdigit = True # Is it the first digit
        for c in line: # Iterate through the characters in the line
            if c.isnumeric(): # If the character is a digit
                if fdigit: first = int(c) # Update first if it is the first digit
                last = int(c) # Always update last
                fdigit = False # No longer the first digit
        ans += ((10 * first) + last) # Update the final answer

print(ans) # Print out the final answer
