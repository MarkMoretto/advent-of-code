
// https://codeforces.com/contest/1613/submission/137930399
// https://www.internalpointers.com/post/differences-between-using-and-typedef-modern-c
#ifndef AOC2021_UTILITIES_H_
#define AOC2021_UTILITIES_H_

#include <iostream>
#include <vector>
#include <string>
#include <math.h>

#define VEC vector


// Types
using LL = long long;
using ULL = unsigned long long;
using LD = long double;
using I = int;
using DB = double;
using S = std::string;

using VLL = std::VEC<LL>;
using VS = std::VEC<S>;

// Macros/aliases
#define nl "\n"
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define clr(x) memset(x, 0, sizeof(x))
#define fil(a, b) memset((a), (b), sizeof(a))
#define sz(q) (I)q.size()
#define pb push_back

// Loop macros
#define FOR(i, x, y) for (int i = (x); i <= (y); i++)
#define FORR(i, x, y) for (int i = (x); i < (y); i++)
#define FORRL(i, x, y) for (LL i = (x); i < (y); i++)
#define DOW(i, x, y) for (int i = (x); i >= (y); i--)

// Constants
const I MOD=1e9+7;
const DB PI=std::acos(-1);

// Templates
template<class Q> bool umin(Q &a, const Q &b){return (a>b?a=b,1:0);}
template<class Q> bool umax(Q &a, const Q &b){return (a<b?a=b,1:0);}


#endif