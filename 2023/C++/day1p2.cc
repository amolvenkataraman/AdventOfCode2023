#include <iostream>
#include <fstream>

// Digit names and values
const int ARR_SIZE = 9;
const std::string DIGIT_NAMES[ARR_SIZE] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
const char DIGIT_VALUES[ARR_SIZE] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};

// insert_ints - Replaces all the occurrences (first characters) of digit names in str with the respective digit values
void insert_ints(std::string& str) {
    int pos = 0; // Start at the beginning of the string

    // Loop while the current position is within the string bounds
    while (pos < str.length()) {
        // Create a populate an array of positions of digit names in the string
        int digit_posns[ARR_SIZE];
        for (int i = 0; i < ARR_SIZE; ++i) {digit_posns[i] = str.find(DIGIT_NAMES[i], pos);}

        // Break out of the loop is no more digits are found
        bool valid = false;
        for (int i = 0; i < ARR_SIZE; ++i) {
            if (digit_posns[i] != std::string::npos) valid = true;
        }
        if (!valid) break;

        // Find the digit that occurs first
        int minval = 0, minpos = 0;
        bool first = true;
        for (int i = 0; i < ARR_SIZE; ++i) { // Iterate through digits
            if ((digit_posns[i] < minval || first) && (digit_posns[i] != std::string::npos)) { // Check if digit occurs before others
                // Update the variables
                minpos = i;
                minval = digit_posns[i];
                first = false;
            }
        }

        // Update the string and reset the position
        str[minval] = DIGIT_VALUES[minpos];
        pos = minval + 1;
    }
}

int main() {    
    std::ifstream f{"input1.txt"}; // Input file
    std::string line;
    int ans = 0;

    // Read lines from the file
    while (std::getline(f, line)) {
        // Replace digit names with digit values
        insert_ints(line);

        int first = 0, last = 0; // First and last digits
        bool fdigit = true; // Is it the first digit
        int len = line.length(); // Get length

        // Iterate through line
        for (int i = 0; i < len; ++i) {
            if (isdigit(line[i])) { // If the current character is a digit
                if (fdigit) first = line[i] - '0'; // Update first if it is the first digit
                last = line[i] - '0'; // Always update last
                fdigit = false; // No longer the first digit
            }
        }
        ans += ((10 * first) + last); // Update the finals answer
    }

    std::cout << ans << std::endl; // Print out the final answer
}
