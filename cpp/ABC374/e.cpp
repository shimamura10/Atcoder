#include<bits/stdc++.h>
using namespace std;

// Ax + By >= Kを満たす、Px + Qyの最小値を求める(O(max(A, B))
long long linearProgramming(int A, int B, long long K, long long P, long long Q) {
    long long minCost = 1e18;
    // A/P > B/Qの場合、Aの方が性能が良い。
    // AをB個使うのは、BをA個使うのよりもコストが高い。
    // よって、BをA個以上使うことはない。
    for (int y = 0; y < A; y++) {
        if (K - y*B < 0) break;
        auto x = (K - y*B + A - 1) / A;
        minCost = min(minCost, x*P + y*Q);
    }
    for (int x = 0; x < B; x++) {
        if (K - x*A < 0) break;
        auto y = (K - x*A + B - 1) / B;
        minCost = min(minCost, x*P + y*Q);
    }
    
    // if (A*Q > B*P) {
    //     for (int y = 0; y < A; y++) {
    //         if (K - y*B < 0) break;
    //         auto x = (K - y*B + A - 1) / A;
    //         minCost = min(minCost, x*P + y*Q);
    //     }
    // } else {
    //     for (int x = 0; x < B; x++) {
    //         if (K - x*A < 0) break;
    //         auto y = (K - x*A + B - 1) / B;
    //         minCost = min(minCost, x*P + y*Q);
    //     }
    // }
    
    return minCost;
}

int N, X;
vector<vector<int>> APBQ;
bool check(int w) {
    long long cost = 0;
    for (const auto& apbq : APBQ) {
        // auto [x, y] = solve(apbq[0], apbq[2], w, apbq[1], apbq[3]);
        // cost += x * apbq[1] + y * apbq[3];
        cost += linearProgramming(apbq[0], apbq[2], w, apbq[1], apbq[3]);
        if (cost > X) {
            return false;
        }
    }
    return true;
}

int binary_search(function<bool(int)> f, int l, int r){
    while (r-l > 1){
        int m = l + (r-l)/2;
        if (f(m)){
            l = m;
        } else {
            r = m;
        }
    }
    return l;
}

int main() {
    cin >> N >> X;
    APBQ.resize(N);
    for (int i = 0; i < N; i++) {
        vector<int> tmp(4);
        cin >> tmp.at(0) >> tmp.at(1) >> tmp.at(2) >> tmp.at(3);
        APBQ.at(i) = tmp;
    }
    int ans = binary_search(check, 0, 1000000001);
    cout << ans << endl;
}