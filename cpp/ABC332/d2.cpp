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
vi row, col;

// binary indexed tree
struct BIT {
    int n;
    vector<long long> bit;
    BIT(int n): n(n), bit(n+1) {}
    void add(int i, long long x) {
        for (int k=i+1; k<=n; k+=k&-k) {
            bit[k] += x;
        }
    }
    long long sum(int i) {
        long long s = 0;
        for (int k=i+1; k>0; k-=k&-k) {
            s += bit[k];
        }
        return s;
    }
};

// 転倒数を求める
ll inversion_number(const vi& a) {
    int n = a.size();
    ll res = 0;
    BIT bit(n);
    for (int i=0; i<n; ++i) {
        res += i - bit.sum(a[i]);
        bit.add(a[i], 1);
    }
    return res;
}

bool check() {
    for (int i=0; i<H; ++i) {
        for (int j=0; j<W; ++j) {
            if (A[row[i]][col[j]] != B[i][j]) {
                return false;
            }
        }
    }
    return true;
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
    row.resize(H);
    col.resize(W);
    for (int i=0; i<H; ++i) {
        row[i] = i;
    }
    for (int i=0; i<W; ++i) {
        col[i] = i;
    }
    int ans = 100;
    do {
        do {
            if (check()) {
                ans = min(ans, (int)inversion_number(row) + (int)inversion_number(col));
            }
        } while (next_permutation(col.begin(), col.end()));
    } while (next_permutation(row.begin(), row.end()));

    cout << (ans == 100 ? -1 : ans) << endl;
}