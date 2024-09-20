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

int H, W;
vvi A, B;
int ans = 10;

bool check() {
    for (int i=0; i<H; ++i) {
        for (int j=0; j<W; ++j) {
            if (A[i][j] != B[i][j]) {
                return false;
            }
        }
    }
    return true;
}

void myswap(int i) {
    if (i < H-1) {
        swap(A[i], A[i+1]);
    } else {
        for (int j=0; j<H; ++j) {
            swap(A[j][i-(H-1)], A[j][i-(H-1)+1]);
        }
    }
}

bool dfs(unordered_set<int>& rest) {
    if (check()) {
        ans = min(ans, H+W-2-(int)rest.size());
        return true;
    }
    vi vrest(rest.begin(), rest.end());
    bool flag = false;
    for (const auto& i: vrest) {
        myswap(i);
        rest.erase(i);
        if (dfs(rest)) {
            flag = true;
        }
        rest.insert(i);
        myswap(i);
    }
    return flag;
}

int main(){
    cin >> H >> W;
    A.resize(H, vi(W));
    B.resize(H, vi(W));
    for (int i=0; i<H; ++i) {
        for (int j=0; j<W; ++j) {
            cin >> A[i][j];
        }
    }
    for (int i=0; i<H; ++i) {
        for (int j=0; j<W; ++j) {
            cin >> B[i][j];
        }
    }
    unordered_set<int> rest;
    for (int i=0; i<H+W-2; ++i) {
        rest.insert(i);
    }
    if (dfs(rest)) {
        cout << ans << endl;
    } else {
        cout << -1 << endl;
    }
}