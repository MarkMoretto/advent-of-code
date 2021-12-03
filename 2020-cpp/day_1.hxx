

// Determine if the sum of two numbers is 2020.
template <class N>
bool is_sum_2020(N n1, N n2) {
    bool res = false;
    if (n1 + n2 == 2020) res = true;
    return res;
}