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

ll calc_dx(ll sx, ll sy, ll tx, ll ty) {
    if ((tx - sx)%2 == 0) {
        return abs(tx-sx)/2;
    } else {
        if (tx - sx > 0) {
            if ((sx + sy)%2 == 0) {
                return abs(tx-sx)/2;
            } else {
                return abs(tx-sx)/2 + 1;
            }
        } else {
            if ((sx + sy)%2 == 0) {
                return abs(tx-sx)/2 + 1;
            } else {

                return abs(tx-sx)/2;
            }
        }
    }
}

int main(){
    ll sx, sy, tx, ty;
    cin >> sx >> sy >> tx >> ty;
    ll ans = 0;
    ll dy = abs(ty-sy);
    auto dx = calc_dx(sx, sy, tx, ty);
    if (dy == 0) {
        cout << dx << endl;
        return 0;
    }
    if (dx == 0) {
        cout << dy << endl;
        return 0;
    }

    dx = max(0LL, dx-dy+1);
    if (tx - sx > 0) {
        if ((tx+ty)%2 != 0) {
            dx = max(0LL, dx-1);
        }
        // ans += max(0LL, tx-sx - abs(ty-sy) + 1LL - ((sx+sy)%2 == 0) - ((tx+ty)%2 != 0));
    } else {
        if ((tx+ty)%2 == 0) {
            dx = max(0LL, dx-1);
        }
    }

    cout << dx + dy << endl;
}