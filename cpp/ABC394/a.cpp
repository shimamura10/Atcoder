#include<bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int cnt2 = 0;
    for (int i = 0; i < S.size(); i++) {
        if (S[i] == '2') cnt2++;
    }

    for (int i = 0; i < cnt2; i++) {
        cout << "2";
    }
    cout << endl;
    return 0;
}