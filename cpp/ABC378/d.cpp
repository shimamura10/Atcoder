#include<bits/stdc++.h>
using namespace std;

void dfs(pair<int, int>&& tmp, vector<string>& S, int K, int& ans, vector<pair<int, int>>& dirs, int H, int W, vector<vector<bool>>& visited) {
    if (K == 0) {
        ans++;
        return;
    }
    for (auto [dx, dy] : dirs) {
        int nx = tmp.first + dx;
        int ny = tmp.second + dy;
        if (nx < 0 || nx >= H || ny < 0 || ny >= W) continue;
        if (S[nx][ny] == '#') continue;
        if (visited[nx][ny]) continue;
        visited[nx][ny] = true;
        dfs({nx, ny}, S, K-1, ans, dirs, H, W, visited);
        visited[nx][ny] = false;
    }
}

int main() {
    int H, W, K;
    cin >> H >> W >> K;
    vector<string> S(H);
    for (int i=0; i<H; i++) {
        cin >> S[i];
    }
    vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int ans = 0;
    vector<vector<bool>> visited(H, vector<bool>(W, false));
    
    for (int h=0; h<H; h++) {
        for (int w=0; w<W; w++) {
            if (S[h][w] == '#') continue;
            visited[h][w] = true;
            dfs({h, w}, S, K, ans, dirs, H, W, visited);
            visited[h][w] = false;
        }
    }
    
    cout << ans << endl;
}