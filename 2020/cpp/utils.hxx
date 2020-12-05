

#ifndef AOC_2020_UTILS_H_
#define AOC_2020_UTILS_H_

#include <iostream>
#include <vector>
#include <numeric>


using uint = std::uint_fast64_t;
using ivec = std::vector<uint>;
const char nl = '\n';
const uint zero = 0;
const uint uone = 1;
const uint utwo = 2;


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

#endif