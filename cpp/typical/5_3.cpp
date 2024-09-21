#include<bits/stdc++.h>
using namespace std;
using ll = long long;

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

constexpr int MOD = 1e9+7;
using mint = Fp<MOD>;

void solve(ll N, int B, int K, vector<int>& C) {
    vector<ll> pow10_2_i(60);
    pow10_2_i[0] = 10%B;
    for (int i = 1; i < 60; i++) {
        pow10_2_i[i] = pow10_2_i[i-1] * pow10_2_i[i-1] % B;
    }

    vector<vector<mint>> doubling(60, vector<mint>(B, 0));
    for (const auto& c : C) {
        doubling[0][c % B] += 1;
    }
    for (int i = 1; i < 60; i++) {
        for (int p = 0; p < B; p++) {
            for (int q = 0; q < B; q++) {
                doubling[i][(p * pow10_2_i[i-1] + q) % B] += doubling[i-1][p] * doubling[i-1][q];
            }
        }
    }

    vector<mint> ans(0);
    for (int i = 0; i < 60; i++) {
        if (N & (1LL << i)) {
            if (ans.empty()) {
                ans = doubling[i];
                continue;
            } 
            vector<mint> tmp(B, 0);
            // doubling[i+j][(p * 10^i + q)%B] = doubling[j][p] * doubling[i][q]
            for (int p = 0; p < B; p++) {
                for (int q = 0; q < B; q++) {
                    tmp[(p * pow10_2_i[i] + q) % B] += ans[p] * doubling[i][q];
                }
            }
            ans = tmp;
        }
    }

    cout << ans[0] << endl;
}

int main() {
    ll N;
    int B, K;
    cin >> N >> B >> K;
    vector<int> C(K);
    for (int i = 0; i < K; i++) {
        cin >> C[i];
    }
    solve(N, B, K, C);
    return 0;
}