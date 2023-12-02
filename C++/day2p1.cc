#include <iostream>
#include <fstream>
#include <sstream>

// Maximum available cubes
const int ARR_SIZE = 3;
const std::string COLOURS[ARR_SIZE] = {"red", "green", "blue"};
const int MAX_VALS[ARR_SIZE] = {12, 13, 14};

int main() {
    std::fstream f{"input2.txt"}; // Input file
    std::string line = ""; // Line in file
    int ans = 0; // Answer

    // Read lines from the file
    while (std::getline(f, line)) {
        bool valid = true; // Assume game is valid at first
        std::string temp = ""; // Temp string to store garbage value
        int gameno = 0;
        std::istringstream iss{line}; // Use stream to read from the line
        iss >> temp; iss >> gameno; iss >> temp; // Read game number and some other garbage text

        // Colour and number of cubes
        int val;
        std::string type;
        while (iss >> val >> type) { // Read in while there are draws remaining
            if (type.back() == ',' || type.back() == ';') type.pop_back(); // Delete , or ;
            for (int i = 0; i < ARR_SIZE; ++i) {
                // Go through the different colours and update the game validity if needed
                if (type == COLOURS[i]) valid = valid && val <= MAX_VALS[i]; 
            }
        }

        if (valid) ans += gameno; // Update the final answer if the game is valid
    }

    std::cout << ans << std::endl; // Print out the final answer
}
