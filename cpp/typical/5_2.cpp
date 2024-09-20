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

vector<vector<mint>> squared(vector<vector<mint>>& A) {
    int N = A.size();
    vector<vector<mint>> res(N, vector<mint>(N, 0));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                res[i][j] += A[i][k] * A[k][j];
            }
        }
    }
    return res;
}

// vector<vector<mint>> mul(vector<vector<mint>>& A, vector<vector<mint>>& B) {
//     int N = A.size();
//     vector<vector<mint>> res(N, vector<mint>(N, 0));
//     for (int i = 0; i < N; i++) {
//         for (int j = 0; j < N; j++) {
//             for (int k = 0; k < N; k++) {
//                 res[i][j] += A[i][k] * B[k][j];
//             }
//         }
//     }
//     return res;
// }

// struct square_matrix {
//     vector<vector<mint>> A;
//     square_matrix(vector<vector<mint>>& A) : A(A) {}
//     square_matrix operator * (const square_matrix& B) {
//         return mul(A, B.A);
//     }

//     const square_matrix mul(const vector<vector<mint>>& A, const vector<vector<mint>>& B) {
//         int N = A.size();
//         vector<vector<mint>> res(N, vector<mint>(N, 0));
//         for (int i = 0; i < N; i++) {
//             for (int j = 0; j < N; j++) {
//                 for (int k = 0; k < N; k++) {
//                     res[i][j] += A[i][k] * B[k][j];
//                 }
//             }
//         }
//         return square_matrix(res);
//     }
// };

template<typename T>
struct matrix {
    vector<vector<T>> A;
    matrix(int N, int M) : A(N, vector<T>(M, 0)) {}
    matrix(vector<vector<T>>& A) : A(A) {}
    vector<T>& operator [] (int i) {
        return A[i];
    }
    matrix operator * (const matrix& B) {
        if (A[0].size() != B.A.size()) {
            throw runtime_error("Invalid matrix size");
        }
        int N = A.size(), M = B.A[0].size(), K = B.A.size();
        vector<vector<T>> res(N, vector<T>(M, 0));
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                for (int k = 0; k < K; k++) {
                    res[i][j] += A[i][k] * B.A[k][j];
                }
            }
        }
        return matrix(res);
    }
    matrix operator *= (const matrix& B) {
        return *this = *this * B;
    }
};

void solve(ll N, int B, int K, vector<int>& C) {
    matrix<mint> A(B, B);
    for (int j = 0; j < B; j++) {
        for (const auto& c : C) {
            for (int f = 0; f < B; f++) {
                if (j == (10*f + c) % B) {
                    A[j][f] += 1;
                }
            }
        }
    }

    matrix<mint> dp(B, 1);
    dp[0][0] = 1;
    for (int i = 0; i < 60; i++) {
        if (N & (1LL << i)) {
            dp = A*dp;
        }
        A *= A;
    }

    cout << dp[0][0] << endl;
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