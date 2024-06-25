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

    ll modpow(ll x, ll n, ll mod) {
        ll res = 1;
        while (n > 0) {
            if (n & 1) {
                res = res * x % mod;
            }
            x = x * x % mod;
            n >>= 1;
        }
        return res;
    }

    ll modinv(ll a, ll mod) {
        return modpow(a, mod - 2, mod);
    }

    ll modfact(ll n, ll mod) {
        ll res = 1;
        for (ll i = 1; i <= n; i++) {
            res = res * i % mod;
        }
        return res;
    }

    ll modcomb(ll n, ll k, ll mod) {
        ll numerator = modfact(n, mod);
        ll denominator = modfact(k, mod) * modfact(n - k, mod) % mod;
        return numerator * modinv(denominator, mod) % mod;
    }

    int main() {
        ll n = 14;
        ll k = 7;
        ll result = modcomb(n, k, MOD);
        cout << result << endl;
        return 0;
    }