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

int main(){
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;

    unordered_set<int> kaibun_bit;
    for (int bit = 0; bit < 1<<K; ++bit) {
        bool is_kaibun = true;
        for (int i = 0; i < K/2; ++i) {
            if ((bit>>i & 1) != (bit>>(K-i-1) & 1)) {
                is_kaibun = false;
                break;
            }
        }
        if (is_kaibun) {
            kaibun_bit.insert(bit);
        }
    }

    // 0がA, 1がB
    vvi dp(N-K+1, vi(1<<K, 0));
    for (int bit = 0; bit < 1<<K; ++bit){
        if (kaibun_bit.contains(bit)) {
            continue;
        }
        bool can = true;
        for (int i = 0; i < K; ++i) {
            if (bit>>i & 1 && S[i] == 'A') {
                can = false;
                break;
            } else if (!(bit>>i & 1) && S[i] == 'B') {
                can = false;
                break;
            }
        }
        if (!can) {
            continue;
        }
        dp[0][bit] = 1;
    }

    for (int i = 0; i < N - K; ++i) {
        for (int bit = 0; bit < 1<<K; ++bit) {
            if (kaibun_bit.contains(bit)) {
                continue;
            }

            auto before_bit = (bit%(1<<(K-1))<<1);
            if (bit>>(K-1) & 1 && S[i+K] != 'A') {
                dp[i+1][bit] += dp[i][before_bit];
                dp[i+1][bit] %= MOD;
                dp[i+1][bit] += dp[i][before_bit+1];
                dp[i+1][bit] %= MOD;
            } else if (!(bit>>(K-1) & 1) && S[i+K] != 'B') {
                dp[i+1][bit] += dp[i][before_bit];
                dp[i+1][bit] %= MOD;
                dp[i+1][bit] += dp[i][before_bit+1];
                dp[i+1][bit] %= MOD;
            }
        }
    }

    ll ans = 0;
    for (const auto& a : dp.back()) {
        ans += a;
        ans %= MOD;
    }

    cout << ans << endl;
}