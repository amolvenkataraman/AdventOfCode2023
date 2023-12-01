#include <iostream>
#include <fstream>

int main() {
    std::ifstream f{"input1.txt"}; // Input file
    std::string line = ""; // Line in file
    int ans = 0; // Answer

    // Read lines from the file
    while (std::getline(f, line)) {
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
        ans += ((10 * first) + last); // Update the final answer
    }

    std::cout << ans << std::endl; // Print out the final answer
}