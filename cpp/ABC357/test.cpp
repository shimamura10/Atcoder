#include <iostream>
using namespace std;

// modint: mod 計算を int を扱うように扱える構造体
template<int MOD> struct Fp {
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

    friend constexpr Fp<MOD> modpow(long long a, long long n) noexcept {
        return modpow(Fp<MOD>(a), n);
    }
};

// template<int MOD>
// constexpr Fp<MOD> modpow(const Fp<MOD> &a, long long n) noexcept {
//     if (n == 0) return 1;
//     auto t = modpow(a, n / 2);
//     t = t * t;
//     if (n & 1) t = t * a;
//     return t;
// }

// template<int MOD>
// constexpr Fp<MOD> modpow(long long a, long long n) noexcept {
//     return modpow(Fp<MOD>(a), n);
// }

int main() {
    // MOD を 1000000007 に設定した Fp クラスのインスタンスを定義
    constexpr int MOD = 1000000007;
    using ModInt = Fp<MOD>;

    // 基数 a と指数 n を定義
    long long a = 2;
    long long n = 10;

    // a の n 乗を MOD で割った余りを計算
    ModInt result = modpow(a, n);

    // 結果を出力
    cout << "2^10 % 1000000007 = " << result << endl;

    return 0;
}
