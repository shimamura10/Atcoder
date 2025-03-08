#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<long long> A(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }

    if (N == 2) {
        cout << "Yes" << endl;
        return 0;
    }

    for (int i=0; i<N-2; i++) {
        if (A[i] * A[i+2] == A[i+1] * A[i+1]) {
            continue;
        } else {
            cout << "No" << endl;
            return 0;
        }
    }

    cout << "Yes" << endl;
}