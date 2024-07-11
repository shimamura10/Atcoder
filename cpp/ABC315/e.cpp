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

int main(){
    int N;
    cin >> N;
    vvi G(N);
    vvi revG(N);
    vi indegree(N, 0);
    for (int i = 0; i < N; ++i){
        int c;
        cin >> c;
        indegree[i] = c;
        for (int j = 0; j < c; ++j){
            int x;
            cin >> x;
            G[x-1].push_back(i);
            revG[i].push_back(x-1);
        }
    }

    // 0に到達するためにたどる必要のある頂点の集合
    vector<bool> reachable(N, false);
    reachable[0] = true;
    queue<int> q;
    q.push(0);
    while (!q.empty()){
        int v = q.front();
        q.pop();
        for (int u : revG[v]){
            if (!reachable[u]){
                reachable[u] = true;
                q.push(u);
            }
        }
    }
    unordered_set<int> must{};
    for (int i = 0; i < N; ++i){
        if (reachable[i]){
            must.insert(i);
        }
    }

    vi stack{};
    for (int i = 0; i < N; ++i){
        if (indegree[i] == 0 && must.find(i) != must.end()){
            stack.push_back(i);
        }
    }
    vi sorted{};
    while (!stack.empty()){
        int v = stack.back();
        stack.pop_back();
        sorted.push_back(v);
        for (int u : G[v]){
            indegree[u]--;
            if (indegree[u] == 0 && must.find(u) != must.end()){
                if (u == 0) {
                    break;
                }
                stack.push_back(u);
            }
        }
    }
    
    for (const auto& e : sorted){
        cout << e+1 << " ";
    }
}