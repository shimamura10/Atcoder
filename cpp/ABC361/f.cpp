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

ll N;

ll binary_search(function<bool(ll, int)> f, ll l, ll r, int b){
    while (r-l > 1){
        int m = l + (r-l)/2;
        if (!f(m, b)){
            r = m;
        } else {
            l = m;
        }
    }
    return r;
}

bool f(ll a, int b) {
    return pow(a, b) <= N;
}

int log(ll N, ll a) {
    int ret = 0;
    ll tmp = a;
    while (tmp <= N){
        tmp *= a;
        ret++;
    }
    return ret;
}

int main(){
    cin >> N;
    ll a = 1;
    ll ans{0};
    ll b = 100;
    while (a*a <= N){
        auto maxA = binary_search(f, 0, N+1, b);
        ans += maxA - a;
        a = maxA;
        b = log(N, a);
    }
    cout << ans << endl;
}