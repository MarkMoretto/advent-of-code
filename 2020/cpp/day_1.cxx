// g++ -Wall -Wextra -o day1 day_1.cxx


#include <iostream>
#include "fs.hxx"
#include "utils.hxx"

int main() {
    STRING PartialPath = R"(data\day-1-input.txt)";
    STRING ParentDir = get_parent_dir();
    STRING FilePath = ParentDir + R"(\)" + PartialPath;
    STRING contents;

    // std::cout << "The parent directory is: " << ParentDir << std::endl;
    // std::cout << "The filepath is: " << FilePath << std::endl;
    
    readfile_test(FilePath, contents);

    std::cout << "The file contents are:\n" << contents << std::endl;

}