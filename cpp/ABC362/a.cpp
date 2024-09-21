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
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;
const int MOD = 998244353;

int main(){
    int r, g, b;
    cin >> r >> g >> b;
    string c;
    cin >> c;
    if (c == "Red") {
        cout << min(g, b) << endl;
    } else if (c == "Green") {
        cout << min(r, b) << endl;
    } else {
        cout << min(r, g) << endl;
    }
}