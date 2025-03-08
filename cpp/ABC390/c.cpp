#include <bits/stdc++.h>
using namespace std;

int main(){
    int H, W;
    cin >> H >> W;
    vector<string> S(H);
    for (int i=0; i<H; i++) {
        cin >> S[i];
    }

    int minH=H, maxH=-1, minW=W, maxW=-1;
    for (int i=0; i<H; i++) {
        for (int j=0; j<W; j++) {
            if (S[i][j] == '#') {
                minH = min(minH, i);
                maxH = max(maxH, i);
                minW = min(minW, j);
                maxW = max(maxW, j);
            }
        }
    }

    if (minH == H) {
        for (int i=0; i<H; i++) {
            for (int j=0; j<W; j++) {
                if (S[i][j] == '?') {
                    cout << "Yes" << endl;
                    return 0;
                }
            }
        }
        cout << "No" << endl;
        return 0;
    }

    for (int i=minH; i<=maxH; i++) {
        for (int j=minW; j<=maxW; j++) {
            if (S[i][j] == '.') {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    cout << "Yes" << endl;
}