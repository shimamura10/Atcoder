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
const int MOD = 998244353;

int H, W, Y;
vvi A;
vector<vector<bool>> visited;
int cnt = 0;
vvi dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

void dfs(int x, int y, int h){
    if (x < 0 || x >= W || y < 0 || y >= H || visited[y][x] || A[y][x] > h){
        return;
    }
    bool tmp = false;
    for (const auto& d : dir){
        int nx = x + d[0];
        int ny = y + d[1];
        if (nx < 0 || nx >= W || ny < 0 || ny >= H || visited[ny][nx]){
            tmp = true;
            break;
        }
    }
    if (!tmp){
        return;
    }

    visited[y][x] = true;
    cnt++;

    for (const auto& d : dir){
        int nx = x + d[0];
        int ny = y + d[1];
        dfs(nx, ny, h);
    }
}

int main(){
    cin >> H >> W >> Y;
    A = vvi(H, vi(W));
    visited = vector<vector<bool>>(H, vector<bool>(W, false));
    unordered_map<int, vector<pair<int, int>>> memo;
    for (int i = 0; i < H; i++){
        for (int j = 0; j < W; j++){
            cin >> A[i][j];
            memo[A[i][j]].emplace_back(j, i);
        }
    }

    for (int h = 1; h <= Y; h++) {
        for (const auto& p : memo[h]){
            dfs(p.first, p.second, h);
        }
        cout << H*W - cnt << endl;
    }
}