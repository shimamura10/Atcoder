#include<bits/stdc++.h>
using namespace std;

void solve(int H, int W, int rs, int cs, int rt, int ct, vector<string>& S) {
    vector<vector<int>> dist(H, vector<int>(W, 1e9));
    queue<int[3]> q;
    pair<int, int> dir[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    q.emplace(rs, cs, -1);
    dist[rs][cs] = -1;

    while(!q.empty()) {
        auto [h, w, cd] = q.front();
        q.pop();
        for (int d=0; d<4; d++) {
            if (cd == d) continue;
            auto nh = h + dir[d].first;
            auto nw = w + dir[d].second;
            while(nh >= 0 && nh < H && nw >= 0 && nw < W && S[nh][nw] == '.' && dist[nh][nw] > dist[h][w]) {
                dist[nh][nw] = dist[h][w]+1;
                q.emplace(nh, nw, d);
                nh += dir[d].first;
                nw += dir[d].second;
            }
        }
    }

    cout << dist[rt][ct] << endl;
}

int main() {
    int H, W;
    cin >> H >> W;
    int rs, cs, rt, ct;
    cin >> rs >> cs >> rt >> ct;
    rs--; cs--; rt--; ct--;
    vector<string> S(H);
    for (int i = 0; i < H; ++i) {
        cin >> S[i];
    }
    solve(H, W, rs, cs, rt, ct, S);
    return 0;
}