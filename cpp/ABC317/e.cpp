#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
#include <unordered_map>
#include <memory>
#include <queue>
#include <unordered_set>
#include <limits>
#include <tuple>
#include <numeric>
#include <set>
#include <random>
#include <string>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;
const ll MOD = 998244353;

void writeEyeline(pair<int, int>& dir, int x, int y, vector<string>& S) {
    int nx = x + dir.first;
    int ny = y + dir.second;
    while (0 <= nx && nx < S.size() && 0 <= ny && ny < S[0].size() && (S[nx][ny] == '.' || S[nx][ny] == '!')) {
        S[nx][ny] = '!';
        nx += dir.first;
        ny += dir.second;
    }
}

int main(){
    int H, W;
    cin >> H >> W;
    vector<string> S(H);
    pair<int, int> start, goal;
    for (int i=0; i<H; ++i) {
        cin >> S[i];
        for (int j=0; j<W; ++j) {
            if (S[i][j] == 'S') {
                start = {i, j};
            } else if (S[i][j] == 'G') {
                goal = {i, j};
            }
        }
    }

    unordered_map<char, pair<int, int>> dirs = {{'^', {-1, 0}}, {'v', {1, 0}}, {'<', {0, -1}}, {'>', {0, 1}}};
    for (int i=0; i<H; ++i) {
        for (int j=0; j<W; ++j) {
            if (dirs.contains(S[i][j])) {
                writeEyeline(dirs[S[i][j]], i, j, S);
            }
        }
    }

    queue<pair<int, int>> q{{start}};
    vector<vector<int>> visited(H, vector<int>(W, -1));
    visited[start.first][start.second] = 0;
    unordered_set<char> NG = {'#', '!', '<', '>', '^', 'v'};
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        for (auto [c, dir]: dirs) {
            int nx = x + dir.first;
            int ny = y + dir.second;
            if (0 <= nx && nx < H && 0 <= ny && ny < W && visited[nx][ny] == -1 && !NG.contains(S[nx][ny])) {
                if (nx == goal.first && ny == goal.second) {
                    cout << visited[x][y] + 1 << endl;
                    return 0;
                }
                visited[nx][ny] = visited[x][y] + 1;
                q.emplace(nx, ny);
            }
        }
    }

    cout << -1 << endl;
}