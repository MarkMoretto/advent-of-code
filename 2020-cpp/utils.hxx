

#ifndef AOC_2020_UTILS_H_
#define AOC_2020_UTILS_H_

#include <iostream>
#include <vector>
#include <numeric>
#include <string>

namespace UTILS {
    using STRING = std::string;

    using uint = std::uint_fast64_t;
    using ivec = std::vector<uint>;
    using svec = std::vector<STRING>;


    const char* nl = "\n";

    const uint zero = 0;
    const uint uone = 1;
    const uint utwo = 2;


    // STRING PartialPath;
    // STRING ParentDir;
    // STRING FilePath = ParentDir + R"(\)" + PartialPath;

    // Content read intake
    // STRING contents;

    void decompose(uint n, ivec &v);

    void explode(STRING s, const char * delim, svec &sout);

    // Create filepath from parent and subpath.
    void set_filepath(const STRING& parent, const STRING& child, STRING& out);
}

#endif