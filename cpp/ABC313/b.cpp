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

void dfs(vvi &G, int v, int p, vi &visited) {
    visited[v] = 1;
    for (int u : G[v]) {
        if (u == p) continue;
        if (visited[u] == 1) {
            continue;
        }
        if (visited[u] == 0) {
            dfs(G, u, v, visited);
        }
    }
}

int main(){
    int N, M;
    cin >> N >> M;
    vvi G(N);
    for (int i=0; i<M; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        G[a].push_back(b);
    }

    for (int i=0; i<N; i++) {
        vi visited(N, 0);
        dfs(G, i, -1, visited);
        if (count(visited.begin(), visited.end(), 1) == N) {
            cout << i+1 << endl;
            return 0;
        }
    }
    cout << -1 << endl;
}