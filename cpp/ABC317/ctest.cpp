#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
#include <unordered_map>
#include <memory>
#include <queue>
#include <unordered_set>
#include <limits>
#include <tuple>
#include <numeric>
#include <set>
#include <random>
#include <string>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;
const ll MOD = 998244353;

vvi permutate(int N) {
    vvi res;
    vi v(N);
    iota(v.begin(), v.end(), 0);
    do {
        res.push_back(v);
    } while (next_permutation(v.begin(), v.end()));
    return res;
}

int main(){
    int res{1};
    for (int i=1; i<=10; i++) {
        res *= i;
    }
    auto perms = permutate(5);
    for (auto perm : perms) {
        for (auto p : perm) {
            cout << p << " ";
        }
        cout << endl;
    }
    // cout << res << endl;
}