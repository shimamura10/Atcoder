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
using vi = vector<ll>;
using vvi = vector<vector<ll>>;
using vl = vector<long long>;
const ll MOD = 998244353;

ll binary_search(function<bool(ll)> f, ll l, ll r){
    while (r-l > 1){
        ll m = l + (r-l)/2;
        if (!f(m)){
            r = m;
        } else {
            l = m;
        }
    }
    return l;
}

ll N;
vl Q, A, B;

bool check(ll x){
    for (ll a=0; a<=x; a++) {
        auto b = x-a;
        bool flag = true;
        for (ll i = 0; i < N; i++) {
            if (Q[i] < A[i]*a + B[i]*b) {
                flag = false;
                break;
            }
        }
        if (flag) {
            return true;
        }
    }
    return false;
}

int main(){
    cin >> N;
    Q.resize(N);
    A.resize(N);
    B.resize(N);
    for (ll i = 0; i < N; i++) cin >> Q[i];
    for (ll i = 0; i < N; i++) cin >> A[i];
    for (ll i = 0; i < N; i++) cin >> B[i];
    cout << binary_search(check, 0, 10000000) << endl;
}