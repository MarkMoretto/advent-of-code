

// #include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <vector>
// #include <array>
// #include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <iomanip>
// #include <limits.h>
// #include <assert.h>
#include <stdexcept>

// https://github.com/jwezorek/AoC_2022/blob/main/src/util.cpp

using namespace std;

const char nl='\n';
const char ws=' ';
const int mod = 998244353, N = 300005, logN = 20, M = 6e6;

using LL = long long;
using LDB = long double;
using DB = double;
using S = string;

using PII = pair<int, int>;
using PLL = pair<LL, LL>;
using PDB = pair<DB, DB>;
using PIS = pair<int, S>;
using PSS = pair<S, S>;

using IVEC =  vector<int>;
using BVEC =  vector<bool>;
using LLVEC = vector<LL>;
using DBVEC = vector<DB>;
using SVEC =  vector<S>;
using SSVEC =  vector<vector<S>>; // Multidim string vector

using PIIV = vector<PII>;
using PLLV = vector<PLL>;
using PDBV = vector<PDB>;

#define MP make_pair
#define PB push_back

const S SMALL_DATA = "data-sm.in";
const S CHALLENGE_DATA = "data.in";

SVEC file_to_str_grid(const S& filepath) {
	SVEC outv;
	S txt;

	std::ifstream ifs(filepath);
	if (!ifs) {
		throw std::runtime_error("Error reading file.");
	}

	while (std::getline(ifs,txt)) outv.push_back(txt);
	return outv;
}










// Driver
void solve() {
	// ...
}




int main() {
	// std::ios_base::sync_with_stdio(false);
	// std::cin.tie(nullptr);
	cin.tie(NULL); cout.tie(NULL);
	freopen("data-sm.in", "r", stdin);
}
