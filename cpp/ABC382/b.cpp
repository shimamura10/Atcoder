#include<bits/stdc++.h>
using namespace std;

int main() {
    int N, D;
    cin >> N >> D;
    string S;
    cin >> S;
    for (int i=N-1; i>=0; i--) {
        if (S[i] == '@') {
            S[i] = '.';
            D--;
            if (D == 0) {
                break;
            }
        }
    }
    cout << S << endl;
    return 0;  
}