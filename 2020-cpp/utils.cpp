
#include "utils.hxx"
using namespace UTILS;

// Print out all lines
template <typename VecType>
void print_vec(VecType &v) {
    for (auto &el : v) {
        std::cout << el << std::endl;
    }
}


template <typename NUM>
void product(NUM &n, std::vector<NUM> *v) {
    n = 1;
    for (NUM &i : *v) {
        n *= i;
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


// Split string by delimiter
void explode(STRING s, const char * delim, svec &sout) {
    std::size_t last = 0;
    std::size_t next = 0;
    while ((next = s.find(delim, last)) != std::string::npos) {
        sout.push_back(s.substr(last, next - last));
        last = next + 1;
    }
    sout.push_back(s.substr(last));
}




// // Set a file path from parent and child string variables.
// void set_filepath(const STRING& parent, const STRING& child, STRING& out) {
//     out = parent + R"(\)" + child;
// }

