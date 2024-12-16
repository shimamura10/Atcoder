#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<pair<int, int>> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i].first >> A[i].second;
    }
    int Q;
    cin >> Q;
    for (int i=0; i<Q; i++) {
        int t, d;
        cin >> t >> d;
        auto r = A[t-1].second;
        auto q = A[t-1].first;
        if (d - r <= 0) {
            cout << r << endl;
            continue;
        } else {
            cout << (d-r-1)/q*q + q + r << endl;
        }
        // auto ans = r;
        // while (ans < d) {
        //     ans += q;
        // }
        // cout << ans << endl;
    }
}