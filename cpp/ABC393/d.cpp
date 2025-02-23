#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    string S;
    cin >> S;
    int cnt1 = 0;
    for (const char &c : S) {
        if (c == '1') cnt1++;
    }
    long long ans = 0;
    int tmp1 = 0;
    for (int i=0; i<N; i++) {
        if (S[i] == '1') {
            tmp1++;
        } else {
            ans += min(tmp1, cnt1-tmp1);
        }
    }
    cout << ans << endl;
}