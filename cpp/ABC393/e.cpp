#include<bits/stdc++.h>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> A(N);
    int MAX = 1000000;
    vector<int> cnts(MAX+1, 0);
    for (int i=0; i<N; i++) {
        cin >> A[i];
        cnts[A[i]]++;
    }

    vector<int> ans(MAX+1, 0);
    for (int i=MAX; i>0; i--) {
        int cnt = 0;
        for (int j=i; j<=MAX; j+=i) {
            cnt += cnts[j];
        }
        if (cnt >= K) {
            for (int j=i; j<=MAX; j+=i) {
                ans[j] = max(ans[j], i);
            }
        }
    }

    for (const auto &a : A) {
        cout << ans[a] << endl;
    }
}