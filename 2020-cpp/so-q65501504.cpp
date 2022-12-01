/**
 * 
 * https://stackoverflow.com/questions/65501504/how-do-i-loop-in-this-if-else-program
 * g++ -Wall -Wextra -o soq so-q65501504.cpp
*/

#include <iostream>
#include <string>

#define MAX_CHAR_LEN 1
#define MAX_ATTEMPTS 3

using SS = std::string;

int no_of_adults;
int no_of_childs;
bool running = true;

void set_people_amt(int&, int&);
int calc_pkg_price(int, int);
void attempt_warning(int);

int main() {

        int price_package;
        int adult_price;
        int child_price;
        int attempts { MAX_ATTEMPTS };
        // char package_code[MAX_CHAR_LEN];

        while (running) {
                SS package_code;
                std::cout << "Enter package code: ";
                std::cin >> package_code;

                if (package_code.size() > 1) {
                        std::cout << "Error: Too many characters. Please enter a single character code." << std::endl;
                        attempts -= 1;
                } else {
                        if (package_code == "X") {
                                std::cout<<"'X' keypress detected!" << std::endl;
                                running = false;
                        }
                        
                        else if (package_code == "A") {
                                adult_price = 40;
                                child_price = 21;
                        }

                        else if (package_code == "B") {
                                adult_price = 23;
                                child_price = 14;
                        }

                        else if (package_code == "C") {
                                adult_price = 38;
                                child_price = 18;
                        }

                        else {
                                std::cout << "Error: Please enter valid code." << std::endl;
                                attempts -= 1;
                        }

                        set_people_amt(no_of_adults, no_of_childs);

                        price_package = calc_pkg_price(adult_price, child_price);

                        std::cout << "Price of package: RM" << price_package << std::endl;
                } 
                if (running && attempts > 0) {
                        attempt_warning(attempts);
                } else {
                        running = false;
                }
        }
        std::cout << "Goodbye!" << std::endl;

}

void set_people_amt(int &adults, int &nonadults) {
        std::cout << "Enter number of adults: ";
        std::cin >> adults;
        std::cout << "Enter number of childs: ";
        std::cin >> nonadults;        
}

int calc_pkg_price(int adult_price, int child_price) {
        return (adult_price * no_of_adults) + (child_price * no_of_childs);
}

void attempt_warning(int attempt_count) {
        std::cout << "You have " << attempt_count << (attempt_count == 1 ? " attempt " : " attempts ") << " remaining." << std::endl;   
}