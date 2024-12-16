#include<bits/stdc++.h>
using namespace std;

int main() {
    int H, W, D;
    cin >> H >> W >> D;
    vector<string> S(H);
    for (int i = 0; i < H; i++) {
        cin >> S[i];
    }

    vector<vector<int>> cnt(H, vector<int>(W, -1));
    queue<pair<int, int>> q;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (S[i][j] == 'H') {
                cnt[i][j] = D;
                q.push({i, j});
            }
        }
    }
    pair<int, int> d[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    while (!q.empty()) {
        auto [i, j] = q.front();
        q.pop();
        if (cnt[i][j] == 0) {
            continue;
        }
        for (auto [di, dj] : d) {
            int ni = i + di;
            int nj = j + dj;
            if (ni < 0 || ni >= H || nj < 0 || nj >= W) {
                continue;
            }
            if (S[ni][nj] == '#') {
                continue;
            }
            if (cnt[ni][nj] >= cnt[i][j]) {
                continue;
            }
            cnt[ni][nj] = cnt[i][j] - 1;
            q.push({ni, nj});
        }
    }

    int ans = 0;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (cnt[i][j] == -1) {
                continue;
            }
            ans++;
        }
    }
    cout << ans << endl;
}
