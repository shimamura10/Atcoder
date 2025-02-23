#include<bits/stdc++.h>
using namespace std;

int main() {
    long long N, M;
    cin >> N >> M;
    unordered_set<long long> S;

    int ans = 0;
    for (int i=0; i<M; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        if (u == v) {
            ans++;
        } else {
            if (S.find(u*N+v) != S.end() || S.find(v*N+u) != S.end()) {
                ans++;
            } else {
                S.insert(u*N+v);
                S.insert(v*N+u);
            }
        }
    }

    cout << ans << endl;
}