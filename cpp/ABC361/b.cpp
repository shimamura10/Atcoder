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

// 線分が共通部分を持つかどうか
bool is_intersect(int a, int b, int c, int d){
    return max(a, c) < min(b, d);
}

int main(){
    int a, b, c, d, e, f;
    cin >> a >> b >> c >> d >> e >> f;
    int g, h, i, j, k, l;
    cin >> g >> h >> i >> j >> k >> l;
    if (is_intersect(a, d, g, j) && is_intersect(b, e, h, k) && is_intersect(c, f, i, l)){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}