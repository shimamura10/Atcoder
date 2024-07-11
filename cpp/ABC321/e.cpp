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

ll log2(ll n) {
    ll res = 0;
    while (n > 1) {
        n >>= 1;
        res++;
    }
    return res;
}

ll fact2(ll n) {
    if (n < 0) {
        return 1;
    }
    static vl ress{1LL};
    while (ress.size() <= n) {
        ress.push_back(ress.back() * 2);
    }
    return ress[n];
}

int main(){
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        ll N, X, K;
        cin >> N >> X >> K;
        ll ans{0};
        auto logX = log2(X), logN = log2(N);
        for (ll up = 0; up <= min(logX, K); up++) {
            auto tmp = logX + K -2*up;
            if (tmp > logN) {
                continue;
            }
            if (up == 0) {
                auto target = X*fact2(K);
                auto targetM = target + fact2(K) - 1;
                ans += tmp == logN? max(min(N,targetM) - target +1, 0LL) : fact2(K);
            } else {
                auto target = (X/fact2(up-1) + (X/fact2(up-1) % 2 == 0 ? 1LL : -1LL)) * fact2(K-up-1);
                auto targetM = target + fact2(K-up-1) - 1;
                ans += tmp == logN? max(min(N, targetM)-target+1, 0LL) : fact2(K-up-1);
            }
        }
        cout << ans << endl;
    }
}