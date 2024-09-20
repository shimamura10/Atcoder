#include <bits/stdc++.h>
#include <ranges>
using namespace std;

// void solve(long long N, long long Q, vector<pair<long long, long long>>& P) {
//   auto rotP = P | views::transform([](pair<long long, long long> p){ return make_pair<long long, long long>(p.first-p.second, p.first+p.second); }) | ranges::to<vector<pair<long long, long long>>>();
//   auto [minX, maxX] = minmax_element(rotP.begin(), rotP.end(), [](pair<long long, long long> a, pair<long long, long long> b){ return a.first < b.first; });
//   auto [minY, maxY] = minmax_element(rotP.begin(), rotP.end(), [](pair<long long, long long> a, pair<long long, long long> b){ return a.second < b.second; });
//   for (const auto& i : views::iota(0, Q)) {
//     long long q; cin >> q;
//     q--;
//     cout << max({abs(minX->first - rotP[q].first), abs(maxX->first - rotP[q].first), abs(minY->second - rotP[q].second), abs(maxY->second - rotP[q].second)}) << endl;
//   }
// }

void old_solve(long long N, long long Q, vector<pair<long long, long long>>& P) {
  vector<pair<long long, long long>> rotP(N);
  for (int i=0; i<N; i++) {
    rotP[i] = make_pair(P[i].first - P[i].second, P[i].first + P[i].second);
  }
  pair<long long, long long> minX = *min_element(rotP.begin(), rotP.end(), [](pair<long long, long long> a, pair<long long, long long> b){ return a.first < b.first; });
  pair<long long, long long> maxX = *max_element(rotP.begin(), rotP.end(), [](pair<long long, long long> a, pair<long long, long long> b){ return a.first < b.first; });
  pair<long long, long long> minY = *min_element(rotP.begin(), rotP.end(), [](pair<long long, long long> a, pair<long long, long long> b){ return a.second < b.second; });
  pair<long long, long long> maxY = *max_element(rotP.begin(), rotP.end(), [](pair<long long, long long> a, pair<long long, long long> b){ return a.second < b.second; });
  for (int i=0; i<Q; i++) {
    long long q; cin >> q;
    q--;
    cout << max({abs(minX.first - rotP[q].first), abs(maxX.first - rotP[q].first), abs(minY.second - rotP[q].second), abs(maxY.second - rotP[q].second)}) << endl;
  }
}

int main() {
  long long N, Q; cin >> N >> Q;
  vector<pair<long long, long long>> P(N);
  for (auto& [x, y] : P) cin >> x >> y;
  old_solve(N, Q, P);
}