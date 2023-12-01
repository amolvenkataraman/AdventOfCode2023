ans = 0 # Answer

ARR_SIZE = 9
DIGIT_NAMES = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
DIGIT_VALUES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# insert_ints - Replaces all the occurrences (first characters) of digit names in str with the respective digit values
def insert_ints(st):
    pos = 0 # Start at the beginning of the string

    # Loop while the current position is within the string bounds
    while (pos < len(st)):
        # Create a populate an array of positions of digit names in the string
        digit_posns = [st[pos:].find(DIGIT_NAMES[i]) for i in range(ARR_SIZE)]
        digit_posns = [i if i == -1 else i + pos for i in digit_posns]

        # Break out of the loop is no more digits are found
        if not any([digit_posns[i] != -1 for i in range(ARR_SIZE)]): break

        # Find the digit that occurs first
        minval = 0; minpos = 0
        first = True
        for i in range(ARR_SIZE): # Iterate through digits
            if ((digit_posns[i] < minval or first) and (digit_posns[i] != -1)): # Chech if digit occurs before others
                # Update the variables
                minpos = i
                minval = digit_posns[i]
                first = False
        
        # Update the string and reset the position
        st = "".join([DIGIT_VALUES[minpos] if n == minval else i for n, i in enumerate(st)])
        pos = minval + 1

    return st

# Open input file ans iterate through lines
with open("input1.txt", "r") as f:
    for line in f.readlines():
        line = insert_ints(line.rstrip())
        first = 0; last = 0 # First and last digits
        fdigit = True # Is it the first digit
        for c in line: # Iterate through the characters in the line
            if c.isnumeric(): # If the character is a digit
                if fdigit: first = int(c) # Update first if it is the first digit
                last = int(c) # Always update last
                fdigit = False # No longer the first digit
        ans += ((10 * first) + last) # Update the final answer

print(ans) # Print out the final answer
