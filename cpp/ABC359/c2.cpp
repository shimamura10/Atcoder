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

ll calc_dx(ll sx, ll sy, ll tx, ll ty){
    auto dx = tx - sx;
    if (dx%2 == 0) {
        return dx/2;
    } else {
        if ((sx + sy)%2 == 0) {
            return dx/2;
        } else {
            return dx/2 + 1;
        }
    }
}

int main(){
    ll sx, sy, tx, ty;
    cin >> sx >> sy >> tx >> ty;
    if (sx > tx) {
        swap(sx, tx);
        swap(sy, ty);
    }
    ll dx = tx - sx;
    ll dy = abs(ty - sy);
    dx = max(0LL, dx - dy + 1);
    cout << dy + max(0LL, calc_dx(sx, sy, sx+dx, sy) - ((tx+ty)%2 != 0));
}