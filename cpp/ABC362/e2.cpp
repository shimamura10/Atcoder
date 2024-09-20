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

using mint = Fp<MOD>;

class TopologicalSort{
    private:
        int N;
        vi indegree;
        vi sorted;
    public:
        vvi G;
        TopologicalSort() : N(0) {}
        TopologicalSort(int N) : N(N), G(N), indegree(N, 0) {}

        void add_edge(int u, int v){
            G[u].push_back(v);
            indegree[v]++;
        }

        vi sort(){
            sorted.clear();
            vi stack{};
            for (int i = 0; i < N; i++) {
                if (indegree[i] == 0 && G[i].size() > 0) {
                    stack.push_back(i);
                }
            }
            while (!stack.empty()) {
                int v = stack.back();
                stack.pop_back();
                sorted.push_back(v);
                for (int u : G[v]) {
                    indegree[u]--;
                    if (indegree[u] == 0) {
                        if (u == 0) {
                            break;
                        }
                        stack.push_back(u);
                    }
                }
            }
            return sorted;
        }
};

int main(){
    int N;
    cin >> N;
    vi A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    unordered_map<int, TopologicalSort> G;
    for (int i = 0; i < N; i++) {
        for (int j = i+1; j < N; j++) {
            auto dif = A[j] - A[i];
            if (G.find(dif) == G.end()) {
                G[dif] = TopologicalSort(N);
            }
            G[dif].add_edge(i, j);
        }
    }

    vector<mint> ans(N, 0);
    for (auto& [dif, g]: G) {
        // if (dif == 0) {
        //     continue;
        // }
        auto sorted = g.sort();
        vector<vector<mint>> dp(N, vector<mint>(N, 0));
        for (int i = 0; i < N; i++) {
            dp[i][0] = 1;
        }
        for (const auto& v: sorted) {
            for (const auto& u: g.G[v]) {
                for (int i = 0; i < N-1; i++) {
                    dp[u][i+1] += dp[v][i];
                }
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                ans[j] += dp[i][j];
            }
        }
    }
    ans[0] = N;
    for (int i = 0; i < N; i++) {
        cout << ans[i] << " ";
    }
}