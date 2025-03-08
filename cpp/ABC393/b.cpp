#include<bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int N = S.size();
    int ans = 0;
    for (int d=1; d<=N/2; d++) {
        for (int i=0; i<N; i++) {
            int j = i + d;
            int k = i + 2*d;
            if (k >= N) break;
            if (S[i] == 'A' && S[j] == 'B' && S[k] == 'C') {
                ans++;
            }
        }
    }
    cout << ans << endl;
}