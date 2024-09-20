#include<bits/stdc++.h>
using namespace std;

void solve(int N, long long K, vector<long long>& A) {
    int MAX_DIGIT = 50;
    vector<vector<long long>> dp(MAX_DIGIT+1, vector<long long>(2, -1));
    dp[0][0] = 0;
    for (int d = 0; d < MAX_DIGIT; ++d) {
        long long mask = 1LL << (MAX_DIGIT - d - 1);
        int num = 0;
        for (const auto& a : A) {
            if (a & mask) {
                ++num;
            }
        }

        // smaller -> smaller
        if (dp[d][1] != -1) dp[d+1][1] = dp[d][1] + max(num, N-num)*mask;

        // equal -> smaller
        if (K & mask) {
            dp[d+1][1] = max(dp[d+1][1], dp[d][0] + num*mask);
        }

        // equal -> equal
        if (K & mask) {
            dp[d+1][0] = dp[d][0] + (N-num)*mask;
        } else {
            dp[d+1][0] = dp[d][0] + num*mask;
        }
    }

    cout << max(dp[MAX_DIGIT][0], dp[MAX_DIGIT][1]) << endl;
}

int main() {
    int N;
    long long K;
    cin >> N >> K;
    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }
    solve(N, K, A);
    return 0;
}