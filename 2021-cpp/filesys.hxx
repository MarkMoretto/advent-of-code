
#ifdef WINDOWS
#include <direct.h>
#define GetCurrentDir _getcwd
#define ChDir _chdir
#else
#include <unistd.h>
#define GetCurrentDir getcwd
#define ChDir chdir
#endif

#ifndef AOC_2021FS_H_
#define AOC_2021_FS_H_

#include <iostream>
#include <string>
#include <fstream>
#include "utils.hxx"

// https://docs.microsoft.com/en-us/cpp/cpp/namespaces-cpp?view=msvc-160
// https://www.educba.com/c-plus-plus-namespace/
namespace FS {

    S get_cwd();
    I change_dir_up();
    S get_parent_dir();


    void readfile_test(S a, S& b);

    // Create filepath from parent and child.
    S create_filepath(S& a, S& b);

    // Create path to data file for a given event day number.
    S filename_by_day(const char * x);
}

#endif