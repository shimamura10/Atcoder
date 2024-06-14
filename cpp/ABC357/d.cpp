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

ll stringMod(string str, ll mod) {
    if (str.size() < 10 && stoll(str) < mod) {
        return stoll(str) % mod;
    }
    ll tmp{stoll(string(str, 16))};
    return stringMod(str.replace(0, 16, to_string(tmp%mod)), mod);
}

int main(){
    ll N;
    cin >> N;
    ll ans{1LL};
    ll cnt{N};
    ll mod{998244353};
    while (cnt > 0) {
        if (cnt%2 == 1) {
            ans = ans*N % mod;
        }
        N = N*N%mod;
        cnt /= 2;
    }

    cout << ans;
}