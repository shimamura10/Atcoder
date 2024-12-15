#include<bits/stdc++.h>
using namespace std;

int main() {
    long long N, M;
    cin >> N >> M;
    vector<pair<int, int>> lrs = vector<pair<int, int>>(N);
    for (int i = 0; i < N; i++) {
        cin >> lrs[i].first >> lrs[i].second;
    }
    sort(lrs.begin(), lrs.end(), [](pair<int, int> a, pair<int, int> b) {
        return a.second < b.second;
    });

    long long not_ans = 0;
    int max_l = 0;
    for (const auto& [l, r] : lrs) {
        if (max_l < l) {
            not_ans += (l - max_l) * (M - r + 1);
            max_l = l;
        }
    }

    cout << M * (M + 1) / 2 - not_ans << endl;
}