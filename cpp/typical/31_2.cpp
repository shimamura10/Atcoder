// #undef LOCAL

#ifdef ONLINE_JUDGE
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#endif

#ifdef LOCAL
// #define _GLIBCXX_DEBUG
#include "../algo/debug.hpp"
#else
#define debug(...) void(0)
#endif

#include <bits/stdc++.h>
using namespace std;

#if __has_include(<atcoder/all>)
// #include <atcoder/all>
// using namespace atcoder;
#endif

constexpr int inf = (1 << 30) - 1;
constexpr long long linf = (1LL << 60) - 1;
using ll = long long;
using ld = long double;
#define len(x) int((x).size())
#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
#define LB(c, x) distance(begin(c), lower_bound(all(c), x))
#define UB(c, x) distance(begin(c), upper_bound(all(c), x))
template <typename F> ll binary_search(F check, ll ok, ll ng, bool CHECK = true) { if(CHECK) assert(check(ok)); while(abs(ok - ng) > 1) { ll mi = (ok + ng) / 2; (check(mi) ? ok : ng) = mi; } return ok; }
template <typename T, typename S> auto min(const T& a, const S& b) { return(a < b ? a : b); }
template <typename T, typename S> auto max(const T& a, const S& b) { return(a > b ? a : b); }
template <typename T, typename S> inline bool chmin(T& a, const S& b) { return(a > b ? a = b, 1 : 0); }
template <typename T, typename S> inline bool chmax(T& a, const S& b) { return(a < b ? a = b, 1 : 0); }
// ------------------------------------------------------------------



void solve() {
    int n; cin >> n;
    vector<ll> W(n), B(n);
    for(int i = 0; i < n; i++) cin >> W[i];
    for(int i = 0; i < n; i++) cin >> B[i];
    vector<vector<ll>> grun(60, vector<ll>(100000, -1));
    auto calc = [&](auto calc, ll w, ll b) -> ll {
        if(grun[w][b] != -1) return grun[w][b];
        if(w == 0 && b <= 1) return grun[w][b] = 0;
        set<int> s;
        if(w - 1 >= 0) s.emplace(calc(calc, w - 1, b + w));
        for(int k = 1; k <= b/2; k++) s.emplace(calc(calc, w, b - k));
        int mex = 0;
        while(s.count(mex)) mex++;
        return grun[w][b] = mex;
    };
    ll ans = 0;
    for(int i = 0; i < n; i++) {
        ans ^= calc(calc, W[i], B[i]);
    }
    cout << (ans == 0 ? "Second" : "First") << endl;

    for (const auto& x : grun | views::take(10)) {
        for (const auto& y : x | views::take(10)) {
            cout << y << " ";
        }
        cout << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // fixed(cout).precision(15);
    int T = 1;
    // cin >> T;
    while(T--) {
        solve();
    }
}