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
    if (res == -1) {
        exit(0);
    }
    return res;
}

int main(){
    int N, K;
    cin >> N >> K;

    // Q = [1, 2, ..., K]でクエリを投げ、その結果をres0とする
    vi Q(K, 0);
    for (int i=0; i<K; i++) {
        Q[i] = i+1;
    }
    int res0 = question(Q);
    int prev_res = res0;

    // edges[i] = [(d, j)] : iとjが同じ値ならd=0, 異なる値ならd=1
    vector<vector<pair<int, int>>> edges(N);
    // 0とK, 1とK+1, ..., K-1と2*K-1をつなぐ
    for (int i=0; i<K; i++) {
        int next = (i+K)%N;
        Q[i%K] = next+1;
        auto cur_res = question(Q);
        if (prev_res == cur_res) {
            edges[i].emplace_back(0,next);
            edges[next].emplace_back(0,i);
        } else {
            edges[i].emplace_back(1,next);
            edges[next].emplace_back(1,i);
        }
        prev_res = cur_res;
    }

    // 0とK+1, 0とK+2, ..., 0とN-1をつなぐ
    for (int i=0; i<K; i++) {
        Q[i] = i+1;
    }
    for (int i=K; i<N-1; i++) {
        int next = (1+i)%N;
        Q[0] = next+1;
        auto cur_res = question(Q);
        if (res0 == cur_res) {
            edges[0].emplace_back(0,next);
            edges[next].emplace_back(0,0);
        } else {
            edges[0].emplace_back(1,next);
            edges[next].emplace_back(1,0);
        }
    }
    
    // edgesを使ってans[0]=0としたときの解を求める
    vi ans(N, -1);
    ans[0] = 0;
    vi cand = {0};
    while (!cand.empty()) {
        int v = cand.back();
        cand.pop_back();
        for (auto& [d, u] : edges[v]) {
            if (ans[u] != -1) continue;
            else if (d == 0) ans[u] = ans[v];
            else ans[u] = 1 - ans[v];
            cand.push_back(u);
        }
    }

    // ans[0]が0であるかどうかを調べ、違っていたらansを反転させる
    int cnt0 = count(ans.begin(), ans.begin()+K, 0);
    if (cnt0%2 == res0) {
        for (auto& a: ans) {
            a = 1 - a;
        }
    }

    // 答えを出力
    cout << "!" << " ";
    for (const auto& a: ans) {
        cout << a << " ";
    }
    cout << endl;
}