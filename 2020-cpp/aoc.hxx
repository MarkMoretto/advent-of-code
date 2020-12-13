
#ifndef AOC_2020_H_
#define AOC_2020_H_

#include <iostream>

#include "utils.hxx"
#include "fs.hxx"

const char* daynum;

STRING PartialPath = filename_by_day(daynum);
STRING ParentDir = get_parent_dir();
STRING FilePath = create_filepath(ParentDir, PartialPath);
STRING contents;

using cout = std::cout;




#endif