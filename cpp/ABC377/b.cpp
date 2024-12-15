#include<bits/stdc++.h>
using namespace std;

int main() {
    vector<string> S(8);
    for (int i = 0; i < 8; i++) {
        cin >> S.at(i);
    }
    vector<vector<bool>> check(8, vector<bool>(8, true));
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (S[i][j] == '#') {
                for (int k = 0; k < 8; k++) {
                    check[i][k] = false;
                    check[k][j] = false;
                }
            }   
        }
    }

    int ans = 0;
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            if (check[i][j]) {
                ans++;
            }
        }
    }
    cout << ans << endl;
}