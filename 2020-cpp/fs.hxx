

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

using namespace UTILS;

// https://docs.microsoft.com/en-us/cpp/cpp/namespaces-cpp?view=msvc-160
// https://www.educba.com/c-plus-plus-namespace/
namespace FS {

    STRING get_cwd();
    int change_dir_up();
    STRING get_parent_dir();


    void readfile_test(STRING a, STRING& b);

    // Create filepath from parent and child.
    STRING create_filepath(STRING& a, STRING& b);

    // Create path to data file for a given event day number.
    STRING filename_by_day(const char * x);
}

#endif