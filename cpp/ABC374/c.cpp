#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> K(N);
    for (int i = 0; i < N; i++) {
        cin >> K.at(i);
    }
    long long ans = accumulate(K.begin(), K.end(), 0LL);
    long long allSum = ans;
    for (int bit = 0; bit < (1 << N); bit++) {
        long long sum = 0;
        for (int i = 0; i < N; i++) {
            if (bit & (1 << i)) {
                sum += K.at(i);
            }
        }
        ans = min(ans, max(sum, allSum - sum));
    }
    cout << ans << endl;
}