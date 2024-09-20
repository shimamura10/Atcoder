#include<bits/stdc++.h>
#include<atcoder/fenwicktree>
using namespace std;

void solve(int N, int M, vector<pair<int, int>>& LR)
{
    sort(LR.begin(), LR.end(), [](pair<int, int>& a, pair<int, int>& b) {
        if (a.second == b.second) return a.first > b.first;
        return a.second < b.second;
    });

    atcoder::fenwick_tree<int> fw(N);
    long long ans = 0;
    for (const auto& [l, r] : LR) {
        ans += fw.sum(0, l);
        fw.add(l, 1);
        fw.add(r-1, -1);
    }

    cout << ans << endl;
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<pair<int, int>> LR(M);
    for (int i = 0; i < M; i++) {
        cin >> LR[i].first >> LR[i].second;
    }

    solve(N, M, LR);
}