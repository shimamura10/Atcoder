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



int main(){
    int H, W;
    cin >> H >> W;
    vector<string> S(H);
    for (int i=0; i<H; ++i){
        cin >> S[i];
    }
    vvi cnt(H, vi(W, -1));
    vector<pair<int, int>> dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    for (int i=0; i<H; ++i) {
        for (int j=0; j<W; ++j) {
            if (S[i][j] == '.') continue;
            cnt[i][j] = 0;
            for (const auto& d : dir) {
                int ni = i + d.first;
                int nj = j + d.second;
                if (ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
                if (S[ni][nj] == '#') continue;
                cnt[ni][nj] = 1;
            }
        }
    }

    vvi entried(H, vi(W, 0));
    for (int i=0; i<H; ++i) {
        for (int j=0; j<W; ++j) {
            if (cnt[i][j] != -1) continue;
            vector<pair<int, int>> stack = {{i, j}};
            vector<pair<int, int>> visited{{i, j}};
            set<int> found1{};
            entried[i][j] = 1;
            while (!stack.empty()) {
                auto [ci, cj] = stack.back();
                stack.pop_back();
                if (cnt[ci][cj] == 1) { continue; }
                for (const auto& d : dir) {
                    int ni = ci + d.first;
                    int nj = cj + d.second;
                    if (ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
                    if (S[ni][nj] == '#') continue;
                    if (cnt[ni][nj] == 1) {
                        found1.insert(ni*W+nj); 
                        continue;
                    }
                    if (entried[ni][nj] == 1) continue;
                    entried[ni][nj] = 1;
                    visited.push_back({ni, nj});
                    stack.push_back({ni, nj});
                }
            }
            int num = visited.size() + found1.size();
            for (const auto& [ci, cj] : visited) {
                cnt[ci][cj] = num;
            }
        }
    }

    int M = 0;
    for (int i=0; i<H; ++i) {
        for (int j=0; j<W; ++j) {
            M = max(M, cnt[i][j]);
        }
    }
    cout << M << endl;
}