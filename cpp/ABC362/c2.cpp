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
const int MOD = 998244353;

int main(){
    int N;
    cin >> N;
    vector<pair<ll, ll>> v(N);
    ll m{0}, M{0};
    for (int i = 0; i < N; i++) {
        cin >> v[i].first >> v[i].second;
        m += v[i].first;
        M += v[i].second;
    }
    if (m > 0 || M < 0) {
        cout << "No" << endl;
        return 0;
    } else {
        cout << "Yes" << endl;
    }

    for (const auto& [l, r]: v) {
        if (M == 0) {
            cout << r << " ";
            continue;
        }
        auto dif = r - l;
        if (M >= dif) {
            M -= dif;
            cout << l << " ";
        } else {
            cout << r - M << " ";
            M = 0;
        }
    }
}