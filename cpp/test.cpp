#include <atcoder/dsu>
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;
const int MOD = 998244353;

int main() {
    vector<int> a = {1, 2, 3, 4, 5};
    for (const auto& x : a | views::drop(3) | views::reverse | views::transform([](int x) { return x * 2; })) {
        cout << x << endl;
    }
}