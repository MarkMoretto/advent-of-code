
#include <iostream>
#include <fstream>
#include <stdio.h>

#include "../utils.hxx"

const S FileName = "test-data01.txt";

int main() {
    std::ifstream ifp;
    ifp.open(FileName);
    if (ifp.fail()){
        std::cout << "Error reading file!" << nl;
        ifp.clear();
        return 0;
    }

    S stmp;
    VS vecstr;
    // while (std::cin.getline(ifp, 256)) {
    while (std::getline(ifp, stmp)) {
        vecstr.pb(stmp);
    }
    for (auto &a : vecstr) {
        std::cout << a << " ";
    }
    std::cout << nl;

}