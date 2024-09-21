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

int N;
vvi edges;
vector<int> colors;
vector<bool> used;
void dfs(int v, int p, int c){
    colors[v] = c;
    used[v] = true;
    for (int u : edges[v]){
        if (u == p || used[u]) continue;
        dfs(u, v, 1-c);
    }
}

int main(){
    cin >> N;
    edges.resize(N);
    colors.resize(N);
    used.resize(N);
    for(int i = 0; i < N-1; i++){
        int a, b;
        cin >> a >> b;
        a--; b--;
        edges[a].push_back(b);
        edges[b].push_back(a);
    }
    dfs(0, -1, 0);
    int cnt = 0;
    for (int i = 0; i < N; i++){
        cnt += colors[i];
    }
    if (cnt >= N/2){
        int cnt2 = 0;
        for (int i = 0; i < N; i++){
            if (colors[i] == 1){
                cout << i+1 << " ";
                cnt2++;
                if (cnt2 == N/2) break;
            }
        }
    } else {
        int cnt2 = 0;
        for (int i = 0; i < N; i++){
            if (colors[i] == 0){
                cout << i+1 << " ";
                cnt2++;
                if (cnt2 == N/2) break;
            }
        }
    }
}