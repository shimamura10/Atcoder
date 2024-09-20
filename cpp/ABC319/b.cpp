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

void check(int i, vector<pair<int, int>>& d) {
    for (const auto& [a, b] : d) {
        if (i % b == 0) {
            cout << a;
            return;
        }
    }
    cout << '-';
}

int main(){
    int N;
    cin >> N;
    vector<pair<int, int>> d{};
    for (int i = 1; i <= 9; i++) {
        if (N % i == 0) {
            d.emplace_back(i, N/i);
        }
    }
    for (int i = 0; i <= N; i++) {
        check(i, d);
    }
}