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

int H, W;
vector<string> S;

int dfs(int i, int j, vvi& cnt, int previ, int prevj, vvi& entried, vvi& exited){
    if (i < 0 || i >= H || j < 0 || j >= W) return 0;
    if (S[i][j] == '#') return 0;
    if (exited[i][j] == 1) return cnt[i][j];
    if (entried[i][j] == 1) return 0;
    entried[i][j] = 1;
    cnt[i][j] = 1;
    vector<pair<int, int>> dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    for (const auto& d : dir){
        int ni = i + d.first;
        int nj = j + d.second;
        if (ni == previ && nj == prevj) continue;
        if (ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
        if (S[ni][nj] == '#') {
            cnt[i][j] = 1;
            break;
        }
        cnt[i][j] += dfs(ni, nj, cnt, i, j, entried, exited);
    }
    exited[i][j] = 1;
    return cnt[i][j];
}

int main(){
    cin >> H >> W;
    S = vector<string>(H);
    vvi cnt(H, vi(W, 0));
    vvi entried(H, vi(W, 0));
    vvi exited(H, vi(W, 0));
    for (int i=0; i<H; ++i){
        cin >> S[i];
    }
    int ans = 0;
    for (int i=0; i<H; ++i){
        for (int j=0; j<W; ++j){
            if (S[i][j] == '#') continue;
            ans = max(ans, dfs(i, j, cnt, i, j, entried, exited));
        }
    }
    cout << ans << endl;    
}