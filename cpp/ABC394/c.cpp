#include<bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    for (int i=0; i<S.size()-1; i++) {
        if (S[i] == 'W' && S[i+1] == 'A') {
            S[i] = 'A';
            S[i+1] = 'C';
            int j = i;
            while (j > 0 && S[j-1] == 'W' && S[j] == 'A') {
                S[j-1] = 'A';
                S[j] = 'C';
                j--;
            }
        }
    }

    cout << S << endl;
    return 0;
}