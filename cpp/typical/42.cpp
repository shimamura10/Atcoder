#include<bits/stdc++.h>
using namespace std;

void solve(int K) {
    if (K % 9 != 0) {
        cout << 0 << endl;
        return;
    }
    long long mod = 1e9+7;
    vector<long long> dp(K+1, 0);
    dp[0] = 1;
    for (int i=1; i<=K; i++) {
        for (int j=0; j<=9; j++) {
            if (i-j >= 0) {
                dp[i] += dp[i-j];
                dp[i] %= mod;
            }
        }
    }
    cout << dp[K] << endl;
}

int main() {
    int K;
    cin >> K;
    solve(K);
    return 0;
}