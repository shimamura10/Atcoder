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

ll dfs(const vector<vector<ll>>& G, unordered_set<int>& rest) {
    vi rest_v(rest.begin(), rest.end());
    ll ret = 0;
    for (int i = 0; i < rest_v.size(); ++i) {
        rest.erase(rest_v[i]);
        for (int j = i+1; j < rest_v.size(); ++j) {
            rest.erase(rest_v[j]);
            ret = max(ret, G[rest_v[i]][rest_v[j]] + dfs(G, rest));
            rest.insert(rest_v[j]);
        }
        rest.insert(rest_v[i]);
    }
    return ret;
}

// ll dfs(int v, const vector<vector<ll>>& G, vi& visited) {
//     visited[v] = 1;
//     ll ret = 0;
//     for (int i = 0; i < N; ++i) {
//         if (visited[i] == 1) continue;
//         visited[i] = 1;
//         auto tmp = G[v][i];
//         for (int j = 0; j < N; ++j) {
//             if (visited[j] == 1) continue;
//             auto tmp2 = dfs(j, G, visited);
//             tmp = max(tmp, G[v][i] + tmp2);
//         }
//         visited[i] = 0;
//         ret = max(ret, tmp);
//     }
//     visited[v] = 0;
//     return ret;
// }

int main(){
    cin >> N;
    vector<vector<ll>> G(N, vector<ll>(N, 0));
    for (int i = 0; i < N; ++i){
        for (int j = i+1; j < N; ++j){
            ll a;
            cin >> a;
            G[i][j] = a;
            G[j][i] = a;
        }
    }

    unordered_set<int> rest;
    for (int i = 0; i < N; ++i){
        rest.insert(i);
    }
    ll ans = 0;
    ans = max(ans, dfs(G, rest));
    cout << ans << endl;
}