

#include "fs.hxx"



STRING get_cwd() {
    // Buffer to hold current path
    char BUFF[FILENAME_MAX];
    GetCurrentDir(BUFF, FILENAME_MAX);
    STRING pwd = BUFF;
    return pwd;
}


// Change directory one level up.
int change_dir_up() {
    char up1[] = "..";
    char *c_ptr = up1;

    int res = ChDir(c_ptr);

    if (res != 0) {
        std::perror("Error changing directory!");
        return -1;
    } else {
        return 0;
    }
}


STRING get_parent_dir() {
    STRING tmps = "";
    int check_cd = change_dir_up();
    if (check_cd == 0) {
        tmps = get_cwd();
    }
    return tmps;
}


// Read file contents;  Output to reference variable.
void readfile_test(STRING filepath, STRING &s) {
    STRING stmp;
    std::ifstream ifs;
    ifs.open(filepath);
    if (ifs.fail()) {
        std::cout << "Error opening file: " << filepath << std::endl;
        ifs.clear();
    } else {
        while (std::getline(ifs, stmp)) {
            s += stmp;
            s += nl;
        }
    }
    s.pop_back(); // Remove last newline char from string.
    ifs.close();
}


STRING create_filepath(STRING& parent, STRING& child) {
    STRING tmps = parent + R"(\)" + child;
    return tmps;
}