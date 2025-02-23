#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long long> K(N);
    vector<vector<int>> A(N, vector<int>());
    for (int i = 0; i < N; i++) {
        cin >> K[i];
        for (int j = 0; j < K[i]; j++) {
            int a;
            cin >> a;
            A[i].push_back(a);
        }
    }

    vector<vector<long long>> B(100001, vector<long long>(N, 0));
    for (int i=0; i<N; i++) {
        for (int j=0; j<K[i]; j++) {
            B[A[i][j]][i]++;
        }
    }
    vector<vector<long long>> cntsame(N, vector<long long>(N, 0));
    for (const auto& b : B) {
        // if (b.size() == 0) continue;
        for (int i=0; i<b.size(); i++) {
            // if (b[i] == b[i+1]) continue;
            for (int j=i+1; j<b.size(); j++) {
                cntsame[i][j] += b[i] * b[j];
            }
        }
    }
    double ans = 0;
    for (int i=0; i<N; i++) {
        for (int j=i+1; j<N; j++) {
            if (i == j) continue;
            ans = max(ans, (double)cntsame[i][j] / (K[i] * K[j]));
        }
    }
    cout << fixed << setprecision(12) << ans << endl;
    // cout << fixed << setprecision(12) << 2.0/3.0 << endl;
    // cout << fixed << setprecision(12) << (double)2/3 << endl;
}