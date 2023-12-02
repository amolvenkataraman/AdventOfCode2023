#include <iostream>
#include <fstream>
#include <sstream>

// Maximum available cubes
const int ARR_SIZE = 3;

int main() {
    std::fstream f{"input2.txt"}; // Input file
    std::string line = ""; // Line in file
    int ans = 0; // Answer

    // Read lines from the file
    while (std::getline(f, line)) {
        // Minimum number of cubes of each type for the game
        std::string colours[ARR_SIZE] = {"red", "green", "blue"};
        int min_vals[ARR_SIZE] = {0, 0, 0};

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
                // Go through the different colours and update the minimum cubes if needed
                if (type == colours[i]) min_vals[i] = std::max(min_vals[i], val);
            }
        }

        // Calculate the product of the different minimum values
        int tmp = 1;
        for (int i = 0; i < ARR_SIZE; ++i) tmp *= min_vals[i];
        ans += tmp; // Update the final answer if the game is valid
    }

    std::cout << ans << std::endl; // Print out the final answer
}
