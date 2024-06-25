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
#include <array>
#include <string>
#include <set>
using namespace std;
const int inf{1000000};

vector<vector<int>> shortestDistance(int sx, int sy, const vector<string>& meiro) {
    int H{static_cast<int>(meiro.size())}, W{static_cast<int>(meiro[0].size())};
    vector<vector<int>> ret(H, vector(W, inf));
    ret[sx][sy] = 0;
    queue<pair<int, int>> can_visit;
    can_visit.push(make_pair(sx, sy));
    const pair<int, int> dir[4] = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};

    while(!can_visit.empty()) {
        auto [x, y] = can_visit.front();
        can_visit.pop();
        for (const auto& [dx, dy] : dir) {
            auto nx{x+dx}, ny{y+dy};
            if (nx<0 || ny<0 || nx>=H || ny>= W) { continue; }
            if (meiro[nx][ny] == '#') { continue; }
            if (ret[nx][ny] > ret[x][y] + 1) {
                ret[nx][ny] = ret[x][y] + 1;
                can_visit.emplace(nx, ny);
            }
            if (ret[nx][ny] == inf) {
                ret[nx][ny] = ret[x][y] + 1;
                can_visit.emplace(nx, ny);
            }
        }
    }

    return ret;
}

vector<bool> dfs(int snum, const vector<vector<int>>& edge) {
    vector<bool> visited(edge.size(), false);
    visited[snum] = true;
    vector<int> can_visit{snum};
    while (!can_visit.empty()) {
        auto now = can_visit.back();
        can_visit.pop_back();
        for (const auto& next : edge[now]) {
            if (!visited[next]) {
                visited[next] = true;
                can_visit.emplace_back(next);
            }
        }
    }
    return visited;
}

int main(){
    int H, W;
    cin >> H >> W;
    vector<string> A{};
    int sx{-1}, sy{-1}, gx{-1}, gy{-1};
    for (int i=0; i<H; i++) {
        string a;
        cin >> a;
        A.push_back(a);
        for (int j=0; j<W; j++) {
            if (a[j] == 'S') {
                sx = i;
                sy = j;
            } else if (a[j] == 'T') {
                gx = i;
                gy = j;
            }
        }
    }
    int N;
    cin >> N;
    vector<array<int, 3>> E{};
    int snum{-1};
    for (int i=0; i<N; i++) {
        int r, c, e;
        cin >> r >> c >> e;
        r--; 
        c--;
        if (r == sx && c == sy) {
            snum = i;
        }
        E.push_back({r, c, e});
    }
    if (snum == -1) {
        cout << "No";
        return 0;
    }
    E.push_back({gx, gy, 0});

    vector<vector<int>> edge(E.size());
    int i{0};
    set<int> can_goal_edges{};
    for (const auto& [sx, sy, e]: E) {
        auto dis = shortestDistance(sx, sy, A);
        int j{0};
        for (const auto& [jx, jy, je] : E) {
            if (i==j) { j++; continue; }
            if (dis[jx][jy] <= e) {
                edge[i].emplace_back(j);
            }
            j++;
        }
        i++;
    }

    if (dfs(snum, edge).back()) {
        cout << "Yes";
        return 0;
    }
    cout << "No";
    return 0;
}