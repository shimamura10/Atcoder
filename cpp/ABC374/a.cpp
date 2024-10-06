#include<bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    // Sの後ろ3文字がsanならYes、それ以外ならNo
    if (S.substr(S.size() - 3) == "san") {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}