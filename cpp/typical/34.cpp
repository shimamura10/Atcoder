#include <bits/stdc++.h>
using namespace std;

void solve(int N, int K, vector<int>& A) {
    int kind = 0;
    int len = 0;
    int ans = 0;
    unordered_map<int, int> cnt;
    int right = 0;
    int left = 0;
    while (right < N) {
        if (cnt[A[right]] == 0) {
            kind++;
        }
        cnt[A[right]]++;
        len++;
        while (kind > K) {
            cnt[A[left]]--;
            if (cnt[A[left]] == 0) {
                kind--;
            }
            len--;
            left++;
        }
        ans = max(ans, len);
        right++;
    }
    cout << ans << endl;
}

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    solve(N, K, A);
}