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

int main(){
    int N;
    cin >> N;
    vvi edges(N);
    vector<pair<int, int>> cntEdge(N);
    for (int i=0; i<N; i++){
        cntEdge[i] = {0, i};
    }
    for(int i = 0; i < N-1; i++){
        int a, b;
        cin >> a >> b;
        a--; b--;
        edges[a].push_back(b);
        edges[b].push_back(a);
        cntEdge[a].first++;
        cntEdge[b].first++;
    }
    priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> pq(cntEdge.begin(), cntEdge.end());
    vi ans{};
    vector<bool> used(N, false);
    while (ans.size() < N/2) {
        auto [c, v] = pq.top();
        pq.pop();
        if (used[v]) continue;
        ans.push_back(v);
        used[v] = true;
        for (const auto& u : edges[v]) {
            used[u] = true;
        }
        for (const auto& u : edges[v]) {
            pq.emplace(--cntEdge[u].first, u);
        }
    }

    for (const auto& a : ans) {
        cout << a+1 << " ";
    }
    // sort(cntEdge.begin(), cntEdge.end(), less<pair<int, int>>());
    // vi check(N, -1);
    // for (const auto& [c, v] : cntEdge) {
    //     if (check[v] != -1) continue;
    //     check[v] = 0;
    //     for (const auto& u : edges[v]) {
    //         if (check[u] != -1) continue;
    //         check[u] = 1;
    //     }
    // }

    // int cnt = 0;
    // for (int i=0; i<N; i++) {
    //     auto c = check[i];
    //     if (c == 0) {
    //         cnt++;
    //         cout << i+1 << " ";
    //     }
    //     if (cnt == N/2) {
    //         break;
    //     }
    // }
}