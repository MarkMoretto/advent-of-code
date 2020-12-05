

#ifdef WINDOWS
#include <direct.h>
#define GetCurrentDir _getcwd
#define ChDir _chdir
#else
#include <unistd.h>
#define GetCurrentDir getcwd
#define ChDir chdir
#endif


#ifndef AOC_2020_FS_H_
#define AOC_2020_FS_H_

#include <iostream>
#include <string>
#include <fstream>
#include "utils.hxx"
// #include <string>
// //#include <windows.h>
// #include <dirent.h>


using STRING = std::string;


STRING get_cwd() {
    // Buffer to hold current path
    char BUFF[FILENAME_MAX];
    GetCurrentDir(BUFF, FILENAME_MAX);
    STRING pwd = BUFF;
    return pwd;
}

void change_dir_up() {
    char up1[] = "..";
    char *c_ptr = up1;

    int res;

    res = ChDir(c_ptr);

    if (res != 0) std::perror("Error changing directory!");
}

STRING get_parent_dir() {
    change_dir_up();
    STRING tmps = get_cwd();
    return tmps;
}


void readfile_test(STRING filepath, STRING &sbuff) {
    STRING s;
    STRING stmp;
    std::ifstream ifs;
    ifs.open(filepath);
    while (std::getline(ifs, stmp)) {
        sbuff += stmp;
        sbuff += nl;
    }
    ifs.close();
    ifs.clear();
}



#endif