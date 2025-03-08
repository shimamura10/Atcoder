#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> P(N);
    for (int i = 0; i < N; i++) {
        cin >> P[i];
    }
    vector<int> Q(N);
    for (int i = 0; i < N; i++) {
        cin >> Q[i];
    }
    vector<int> ans(N, 0);
    for (int i=0; i<N; i++) {
        ans[Q[i]-1] = Q[P[i]-1];
    }
    for (const auto& a : ans) {
        cout << a << " ";
    }
    cout << endl;
    return 0;
}