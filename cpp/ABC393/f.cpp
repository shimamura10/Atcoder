#include<bits/stdc++.h>
using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    vector<vector<int>> Queries(Q, vector<int>(3));
    for (int i=0; i<Q; i++) {
        Queries[i][0] = i;
        cin >> Queries[i][1] >> Queries[i][2];
    }
    sort(Queries.begin(), Queries.end(), [](const vector<int> &a, const vector<int> &b) {
        return a[1] < b[1];
    });

    vector<int> dp(N+1, 1000000001);
    vector<int> ans(Q);
    int q = 0;
    for (int i=0; i<N; i++) {
        auto idx = lower_bound(dp.begin(), dp.end(), A[i]) - dp.begin();
        dp[idx] = A[i];
        while (q < Q && Queries[q][1] == i+1) {
            ans[Queries[q][0]] = upper_bound(dp.begin(), dp.end(), Queries[q][2]) - dp.begin();
            q++;
        }
    }

    for (const auto &a : ans) {
        cout << a << endl;
    }
}