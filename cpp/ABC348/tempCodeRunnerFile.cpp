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

int main(){
    int H, W;
    cin >> H >> W;
    vector<string> A{};
    for (int i=0; i<H; i++) {
        string a;
        cin >> a;
        A.push_back(a);
    }
    int N;
    cin >> N;
    vector<array<int, 3>> E{};
    unordered_map<string, int> mE{};
    for (int i=0; i<N; i++) {
        int r, c, e;
        cin >> r >> c >> e;
        E.push_back({r-1, c-1, e});
        mE.emplace(to_string(r-1)+to_string(c-1), i);
    }

    vector<vector<int>> edge(N);
    const pair<int, int> dir[4] = {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};
    int i{0};
    set<int> can_goal_edges{};
    auto compare = [](array<int, 3>& a, array<int, 3>& b) {
        return a[2] < b[2];
    };
    for (const auto& [sx, sy, e]: E) {
        vector<vector<bool>> visited(H, vector(W, false));
        priority_queue<array<int, 3>, vector<array<int, 3>>, decltype(compare)> can_visit;
        can_visit.push({sx, sy, e});
        visited[sx][sy] = true;
        while (!can_visit.empty()) {
            auto [now_x, now_y, now_e] = can_visit.top();
            can_visit.pop();
            if (now_e == 0 || visited[now_x][now_y]) {
                continue;
            }
            for (const auto& [dx, dy] : dir) {
                int next_x{now_x + dx};
                int next_y{now_y + dy};

                if (next_x < 0 || next_x >= H || next_y < 0 || next_y >= W) {
                    continue;
                }
                if (A[next_x][next_y] == '#') {
                    continue;
                }

                if (A[next_x][next_y] == 'T') {
                    can_goal_edges.insert(i);
                }

                can_visit.push({next_x, next_y, now_e-1});
                if (mE.count(to_string(next_x)+to_string(next_y)) == 1) {
                    edge[i].push_back(mE[to_string(next_x)+to_string(next_y)]);
                }
            }
            visited[now_x][now_y] = true;
        }
        i++;
    }

    int sx{-1};
    int sy{-1};
    for (int i=0; i<H; i++) {
        for (int j=0; j<W; j++) {
            if (A[i][j] == 'S') {
                sx = i;
                sy = j;
            }
        }
    }
    if (mE.count(to_string(sx) + to_string(sy)) == 0) {
        cout << "No";
        return 0;
    }

    vector<bool> visited(N, false);
    vector<int> can_visit{mE[to_string(sx) + to_string(sy)]};
    while (!can_visit.empty()) {
        auto now = can_visit.back();
        can_visit.pop_back();
        if (can_goal_edges.count(now) == 1) {
            cout << "Yes";
            return 0;
        }
        for (const auto& next : edge[now]) {
            if (visited[next]) {
                continue;
            }
            visited[next] = true;
            can_visit.emplace_back(next);
        }
    }
    cout << "No";
    return 0;
}