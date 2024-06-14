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
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

int divide2num (ll num) {
    int ret{0};
    while (num >1) {
        num /= 2;
        ret++;
    }
    return ret;
}

int main(){
    ll L, R;
    cin >> L >> R;
    vector<pair<ll, ll>> answer;
    while (L < R) {
        auto i = divide2num(L);
        while ( (1<<i) + L > R) {
            i--;
        }
        answer.emplace_back(L, L+(1<<i));
        L += 1<<i;
    }

    cout << answer.size() << endl;
    for (const auto& [L, R] : answer) {
        cout << L << " " << R << endl;
    }
}