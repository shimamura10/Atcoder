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

int question(vi &Q) {
    cout << "?" << " ";
    for (int j=0; j<Q.size(); j++) {
        cout << Q[j] << " ";
    }
    cout << endl;
    int res;
    cin >> res;
    return res;
}

int main(){
    int N, K;
    cin >> N >> K;

    vi Q(K, 0);
    for (int i=0; i<K; i++) {
        Q[i] = i+1;
    }
    int res0 = question(Q);
    int prev_res = res0;

    vector<vector<pair<int, int>>> edges(N);
    for (int i=0; i<N; i++) {
        int next = (i+K)%N;
        Q[i] = next+1;
        if (prev_res == question(Q)) {
            edges[i].emplace_back(0,next);
            edges[next].emplace_back(0,i);
        } else {
            edges[i].emplace_back(1,next);
            edges[next].emplace_back(1,i);
        }
    }
    
    vi ans(N, -1);
    ans[0] = 0;
    vi cand = {0};
    while (!cand.empty()) {
        int v = cand.back();
        cand.pop_back();
        for (auto& [d, u] : edges[v]) {
            if (ans[u] != -1) continue;
            ans[u] = d;
            cand.push_back(u);
        }
    }

    int cnt0 = count(ans.begin(), ans.begin()+K, 0);
    if (cnt0%2 == res0) {
        for (auto& a: ans) {
            a = 1 - a;
        }
    }

    cout << "!" << " ";
    for (const auto& a: ans) {
        cout << a << " ";
    }
    cout << endl;
}