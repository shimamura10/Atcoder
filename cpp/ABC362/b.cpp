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

int dis(int x1, int y1, int x2, int y2){
    return abs(x1 - x2)*abs(x1 - x2) + abs(y1 - y2)*abs(y1 - y2);
}

int main(){
    int xa, ya, xb, yb, xc, yc;
    cin >> xa >> ya >> xb >> yb >> xc >> yc;
    auto d1 = dis(xa, ya, xb, yb);
    auto d2 = dis(xb, yb, xc, yc);
    auto d3 = dis(xc, yc, xa, ya);
    if (d1 == d2 + d3 || d2 == d1 + d3 || d3 == d1 + d2) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}