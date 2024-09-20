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

ll binary_search(function<bool(ll)> f, ll l, ll r){
    while (r-l > 1){
        ll m = l + (r-l)/2;
        if (f(m)){
            r = m;
        } else {
            l = m;
        }
    }
    return r;
}

int N, M;
vl L{};

bool check(ll x) {
    int cnt = 0;
    ll tmp = 0;
    for (const auto& l : L) {
        if (l > x) return false;
        if (tmp + l <= x) {
            tmp += l+1;
        } else {
            cnt++;
            tmp = l+1;
        }
    }
    return cnt < M;
}

int main(){
    cin >> N >> M;
    L.resize(N);
    for (int i = 0; i < N; i++) {
        cin >> L[i];
    }
    cout << binary_search(check, 0, 1e17) << endl;
}