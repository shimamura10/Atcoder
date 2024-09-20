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

// modint: mod 計算を int を扱うように扱える構造体
template<int MOD> struct Fp {
    static vector<Fp> facts, ifacts;
    long long val;
    constexpr Fp(long long v = 0) noexcept : val(v % MOD) {
        if (val < 0) val += MOD;
    }
    constexpr int getmod() { return MOD; }
    constexpr Fp operator - () const noexcept {
        return val ? MOD - val : 0;
    }
    constexpr Fp operator + (const Fp& r) const noexcept { return Fp(*this) += r; }
    constexpr Fp operator - (const Fp& r) const noexcept { return Fp(*this) -= r; }
    constexpr Fp operator * (const Fp& r) const noexcept { return Fp(*this) *= r; }
    constexpr Fp operator / (const Fp& r) const noexcept { return Fp(*this) /= r; }
    constexpr Fp& operator += (const Fp& r) noexcept {
        val += r.val;
        if (val >= MOD) val -= MOD;
        return *this;
    }
    constexpr Fp& operator -= (const Fp& r) noexcept {
        val -= r.val;
        if (val < 0) val += MOD;
        return *this;
    }
    constexpr Fp& operator *= (const Fp& r) noexcept {
        val = val * r.val % MOD;
        return *this;
    }
    constexpr Fp& operator /= (const Fp& r) noexcept {
        long long a = r.val, b = MOD, u = 1, v = 0;
        while (b) {
            long long t = a / b;
            a -= t * b; swap(a, b);
            u -= t * v; swap(u, v);
        }
        val = val * u % MOD;
        if (val < 0) val += MOD;
        return *this;
    }
    constexpr bool operator == (const Fp& r) const noexcept {
        return this->val == r.val;
    }
    constexpr bool operator != (const Fp& r) const noexcept {
        return this->val != r.val;
    }
    friend constexpr ostream& operator << (ostream &os, const Fp<MOD>& x) noexcept {
        return os << x.val;
    }
    friend constexpr Fp<MOD> modpow(const Fp<MOD> &a, long long n) noexcept {
        if (n == 0) return 1;
        auto t = modpow(a, n / 2);
        t = t * t;
        if (n & 1) t = t * a;
        return t;
    }
    friend Fp<MOD> fact (const Fp<MOD> &n) noexcept {
        while ((int)facts.size() <= n.val) {
            facts.push_back(facts.back() * Fp<MOD>((int)facts.size()));
        }
        return facts[n.val];
    }
    friend Fp<MOD> ifact (const Fp<MOD> &n) noexcept {
        while ((int)ifacts.size() <= n.val) {
            ifacts.push_back(ifacts.back() / Fp<MOD>((int)ifacts.size()));
        }
        return ifacts[n.val];
    }
    friend Fp<MOD> cmp(const Fp<MOD> &n, const Fp<MOD> &r) {
        if (n.val < 0 || r.val < 0) return 0;
        Fp<MOD> tmpr = min(r.val, n.val - r.val);
        return fact(n) * ifact(tmpr) * ifact(n - tmpr);
    }
};

template<int MOD> vector<Fp<MOD>> Fp<MOD>::facts = {1, 1};
template<int MOD> vector<Fp<MOD>> Fp<MOD>::ifacts = {1, 1};

const int MOD = 998244353;
using mint = Fp<MOD>;

int main(){
    int K;
    cin >> K;
    vi C(26);
    for (int i = 0; i < 26; i++) cin >> C[i];
    vector<vector<mint>> dp(27, vector<mint>(K + 1, 0));
    dp[0][0] = 1;
    for (int i = 0; i < 26; i++) {
        for (int j = 0; j <= K; j++) {
            for (int k = 0; k <= min(j, C[i]); k++) {
                dp[i + 1][j] += dp[i][j - k] * cmp(mint(j), mint(k));
            }
        }
    }
    cout << accumulate(dp[26].begin()+1, dp[26].end(), mint{0}) << endl;
}