#include<bits/stdc++.h>
using namespace std;

int main() {
    string S, T;
    cin >> S >> T;

    int m = min(S.size(), T.size());
    for (int i = 0; i < m; i++) {
        if (S[i] == T[i]) {
            continue;
        } else {
            cout << i+1 << endl;
            return 0;
        }
    }
    if (S.size() != T.size()) {
        cout << m+1 << endl;
    } else {
        cout << 0 << endl;
    }
}