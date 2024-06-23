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

int N;
int ans{0};
vvi edges;

// 実質グラフの直径を求めているらしい
int dfs(int v, int p){
    int M = 0, M2 = 0;
    for (auto u : edges[v]){
        if (u == p) continue;
        int d = dfs(u, v);
        if (d > M){
            M2 = M;
            M = d;
        } else if (d > M2){
            M2 = d;
        }
    }
    ans = max(ans, M + M2 + 1);
    return M + 1;
}

int main(){
    cin >> N;
    edges.resize(N);
    for (int i=0; i<N-1; ++i){
        int a, b;
        cin >> a >> b;
        a--; b--;
        edges[a].emplace_back(b);
        edges[b].emplace_back(a);
    }

    dfs(0, -1);
    cout << ans << endl;
}