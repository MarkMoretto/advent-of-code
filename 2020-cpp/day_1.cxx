// g++ -std=c++17 -Wall -Wextra -o day1 day_1.cxx


#include <iostream>
#include <algorithm>
#include "fs.hxx"
#include "utils.hxx"
#include "day_1.hxx" // explode()

int main() {
    STRING PartialPath = R"(data\day-1-input.txt)";
    STRING ParentDir = get_parent_dir();
    STRING FilePath = ParentDir + R"(\)" + PartialPath;
    STRING contents;
    svec lines; // string vector for holding output lines of textfile.
    const char* delimiter = "\n"; // Delimiter for splitting lines of text file.
    
    ivec ivLINES; // Integer vector for converted string vector values.
    // ivec selected; // Integer vector for selected values.
    bool pair_found = false; // whether or not a pair of values was found.

    // std::cout << "The parent directory is: " << ParentDir << std::endl;
    // std::cout << "The filepath is: " << FilePath << std::endl;
    
    readfile_test(FilePath, contents);

    // Explode or split string by a delimiter.
    explode(contents, delimiter, lines);

    // Convert to integer (since we know the data type
    ivLINES.reserve(sizeof(lines));

    for (STRING &abc : lines) {
        ivLINES.push_back(std::stoi(abc));
    }

    // Clear string vector
    lines.erase(lines.begin() + lines.size());

    // Sort vector of strings
    // std::sort(lines.begin(), lines.end(), std::greater<svec>());

    // Sort vector of numerical values
    std::sort(ivLINES.begin(), ivLINES.end());

    // Print out all lines
    // print_vec(ivLINES);
    


    // Split or bisect vector
    std::size_t middle = ivLINES.size() / 2;
    ivec svLOW(ivLINES.begin(), ivLINES.begin() + middle);
    ivec svHI(ivLINES.begin() + middle, ivLINES.end());
    

    for (int x : svLOW) {
        for (int y : svLOW) {
            // If x != y and the two numbers add up to 2020.
            if ((x != y) && (is_sum_2020(x, y))) {

                // Multiply the two numbers and output results.
                int output(x * y);

                std::cout << "The product of " << x << " and " << y << " is: " << output << std::endl;

                // Update variable to exit function early.
                pair_found = true;
                break;
            }
        }
    }


    // std::cout << "The file contents are:\n" << contents << std::endl;
    return 0;
}