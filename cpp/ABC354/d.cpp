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

ll calcX(ll x, ll y) {
    if (y == 0 || x == 0) {return 0;}
    ll black[2][4] = {{0, 1, 3, 4},
                    {0, 2, 3, 3}};
    ll mod = x%4;
    return x - mod + black[y%2][x%4];
}

ll calcY(ll x, ll y) {
    if (y == 0 || x == 0) {return 0;}
    ll black[4][4] = {{0, 1, 1, 2},
                    {0, 2, 3, 5},
                    {0, 1, 3, 4},
                    {0, 0, 1, 1}};
    ll mod = y%4;
    return y - mod + black[x%4][y%4];
}



int upper4(int a) {
    if (a%4 == 0) {
        return a;
    }
    return a + 4 - a%4;
}

ll resolve (ll& a, ll& b, ll& c, ll& d) {
    ll black[4][4] = {{0, 1, 0, 1},
                        {1, 2, 1, 2},
                        {2, 1, 2, 1},
                        {1, 0, 1, 0}};
    ll ret{upper4(c) * upper4(d)};
    // 下側を引く
    for (int y=1; y<=b%4; y++) {
        ret -= calcX(c, y);
    }
    // 左側を引く
    for (int x=1; x<=a%4; x++) {
        ret -= calcY(x, d);
    }
    // 上側を引く
    for (int y=d+1; y<=upper4(d); y++) {
        ret -= calcX(c, y);
    }
    // 右側を引く
    for (int x=c+1; x<=upper4(c); x++) {
        ret -= calcY(x, d);
    }
    // 左下を足す
    for (int x=1; x<=a; x++) {
        for (int y=1; y<= b; y++) {
            ret += black[x%4][y%4];
        }
    }
    // 左上を足す
    for (int x=1; x<=a; x++) {
        for (int y=d+1; y<=upper4(d); y++) {
            ret += black[x%4][y%4];
        }
    }
    // 右下を足す
    for (int x=c+1; x<=upper4(c); x++) {
        for (int y=1; y<=b; y++) {
            ret += black[x%4][y%4];
        }
    }
    // 右上を足す
    for (int x=c+1; x<=upper4(c); x++) {
        for (int y=d+1; y<=upper4(d); y++) {
            ret += black[x%4][y%4];
        }
    }
    return ret;
}

int main(){
    ll A, B, C, D;
    cin >> A >> B >> C >> D;
    if (A < 0) {
        auto dif = upper4(-A);
        A += dif;
        C += dif;
    } else {
        auto dif = A/4*4;
        A -= dif;
        C -= dif;
    }
    if (B < 0) {
        auto dif = upper4(-B);
        B += dif;
        D += dif;
    } else {
        auto dif = B/4*4;
        B -= dif;
        D -= dif;
    }

    cout << resolve(A, B, C, D);
}