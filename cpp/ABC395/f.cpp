#include<bits/stdc++.h>
using namespace std;

int main() {
    int N, X;
    cin >> N >> X;
    vector<long long> U(N), D(N);
    vector<pair<long long, int>> tmp(N);
    for (int i = 0; i < N; i++) {
        cin >> U[i] >> D[i];
        tmp[i] = {U[i], i};
    }
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq(tmp.begin(), tmp.end());
    long long ans = 0;
    while (!pq.empty()) {
        auto [u, i] = pq.top();
        pq.pop();
        if (U[i] < u) continue;
        // vector<int> v{max(0, i-1), min(N-1, i+1)};
        for (int j : {max(0, i-1), min(N-1, i+1)}) {
            auto dif = U[i] - U[j];
            if (dif > X) {
                auto tmp = U[j] + X;
                ans += U[i] - tmp;
                U[i] = tmp;
            } else if (dif < -X) {
                auto tmp = U[i] + X;
                ans += U[j] - tmp;
                U[j] = tmp;
                pq.push({U[j], j});
            }
        }
    }

    vector<long long> S(N);
    for (int i = 0; i < N; i++) {
        S[i] = U[i] + D[i];
    }
    auto minS = *min_element(S.begin(), S.end());
    for (const auto& s : S) {
        ans += s - minS;
    }

    cout << ans << endl;
}