#include<bits/stdc++.h>
using namespace std;

int main() {
    int H, W, D;
    cin >> H >> W >> D;
    vector<string> S(H);
    for (int i = 0; i < H; i++) {
        cin >> S[i];
    }
    
    int ans = 0;
    for (int i = 0; i < H*W; i++) {
        int xi = i % W;
        int yi = i / W;
        if (S[yi][xi] != '.') {
            continue;
        }
        for (int j = i+1; j < H*W; j++) {
            int xj = j % W;
            int yj = j / W;
            if (S[yj][xj] != '.') {
                continue;
            }
            int tmp = 0;
            for (int x = 0; x < W; x++) {
                for (int y = 0; y < H; y++) {
                    if (S[y][x] != '.') {
                        continue;
                    }
                    if (abs(xi-x) + abs(yi-y) <= D || abs(xj-x) + abs(yj-y) <= D) {
                        tmp++;
                    }
                }
            }
            ans = max(ans, tmp);
        }
    }
    cout << ans << endl;
}