

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



STRING get_cwd();

int change_dir_up();


STRING get_parent_dir();


void readfile_test(STRING, STRING&);


#endif