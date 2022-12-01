// g++ -Wall -Wextra -o bin\core core.cxx
// g++ -std=c++17 -Wall -Wextra -o bin\core core.cxx
// https://code.visualstudio.com/docs/editor/variables-reference

#include <iostream>
#include "fs.hxx"
#include "utils.hxx"

using namespace UTILS;

const char* daynum = "13";

int main() {

    STRING PartialPath = FS::filename_by_day(daynum);
    STRING ParentDir = FS::get_parent_dir();
    STRING FilePath = FS::create_filepath(ParentDir, PartialPath);
    // STRING contents;
    std::cout << FilePath << nl;
}
