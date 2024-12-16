#include<bits/stdc++.h>
using namespace std;

bool next(vector<int>& A) {
    int N = A.size();
    for (int i=N-1; i>=0; i--) {
        if (A[i] == 0) {
            continue;
        }
        if (i == 0) {
            return false;
        }
        A[i]--;
        A[i-1]++;
        int tmp = 0;
        for (int j=i; j<N; j++) {
            tmp += A[j];
            A[j] = 0;
        }
        A[N-1] = tmp;
        return true;
    }
    return false;
}

long long cmb(int n, int r) {
    long long ans = 1;
    for (int i=0; i<r; i++) {
        ans *= n-i;
        ans /= i+1;
    }
    return ans;
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> A(N+1, 0);
    auto amari = M - 10*(N-1) - 1;
    A[N] = amari;
    int now = N;
    cout << cmb(N+amari, amari) << endl;
    do {
        int ans = 1 + A[0];
        for (int i=0; i<N; i++) {
            cout << ans << " ";
            ans += 10 + A[i+1];
        }
        cout << endl;
    } while (next(A));
}