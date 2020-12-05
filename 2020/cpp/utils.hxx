

#ifndef AOC_2020_UTILS_H_
#define AOC_2020_UTILS_H_

#include <iostream>
#include <vector>
#include <numeric>
#include <string>


using uint = std::uint_fast64_t;
using ivec = std::vector<uint>;
using svec = std::vector<std::string>;

const char nl = '\n';

const uint zero = 0;
const uint uone = 1;
const uint utwo = 2;


// Print out all lines
template <typename VecType>
void print_vec(VecType &v) {
    for (auto &el : v) {
        std::cout << el << std::endl;
    }
}

void decompose(uint n, ivec &v) {
    // Prime decomposition of a number.
    uint i = 2;

    // In addition we define f(1)=1.
    while (n != 1) {
        while (n % i == 0) {
            // v.push_back(i);
            v.push_back(utwo);
            n /= i;
        }
        ++i;
    }
}


void product(uint &n, ivec *v) {
    n = 1;
    for (uint &i : *v) {
        n *= i;
    }  
}


// Split string by delimiter
void explode(std::string s, const char * delim, svec &sout) {
    std::size_t last = 0;
    std::size_t next = 0;
    while ((next = s.find(delim, last)) != std::string::npos) {
        sout.push_back(s.substr(last, next - last));
        last = next + 1;
    }
    sout.push_back(s.substr(last));
}



#endif