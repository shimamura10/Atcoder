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
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;

ll mod{998244353};

int cnt2(const ll& x) {
    auto _x = x;
    int ret{0};
    while (_x > 1) {
        ret++;
        _x /= 2;
    }
    return ret;
}

ll fact2(int n) {
    static vl ret{1};
    if (static_cast<int>(ret.size()) <= n) {
        ret.emplace_back(ret.back()*2%mod);
    }
    return ret[n];
}

int main(){
    ll N, M;
    cin >> N >> M;

    ll ans{0};
    auto n2{cnt2(N)};
    for (int i=0; i<=n2; i++) {
        if ( !(M>>i & 1) ) { continue; }
        ll left{ N>>(i+1) };
        ll right{ N%static_cast<ll>(pow(2,i))+1 };
        ans += left*static_cast<ll>(pow(2,i))%mod;
        if ( N>>i & 1 ) {
            ans += right;
        }
        ans %= mod;
    }

    cout << ans;

    // vl A{0};
    // auto n2{cnt2(N)};
    // for (int i=0; i<=n2; i++) {
    //     ll d{0};
    //     for (const auto& a : A) {
    //         d += a;
    //         d %= mod;
    //     }
    //     if (M >> i & 1) {
    //         d += fact2(i);
    //     }
    //     A.emplace_back(d%mod);
    // }

    // ll ans{0};
    // for (int i=0; i<=n2; i++) {
    //     if (N >> i & 1) {
    //         ans += A[i+1];
    //         ans %= mod;
    //     }
    // }
    // cout << ans;
}