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
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;
using pii = pair<int, int>;

int main(){
    int N;
    cin >> N;
    auto compare = [](pair<int, int> a, pair<int, int> b) {
        return a.first > b.first;
    };
    priority_queue<pair<int, int>, vector<pii> ,decltype(compare)> que{compare};
    for (int i=0; i<N; i++) {
        int l, r;
        cin >> l >> r;
        que.emplace(l, 1);
        que.emplace(r, -1);
    }
    ll kind{0}, ans{0};
    while (!que.empty()) {
        const auto now = que.top();
        ll plus{0}, minus{0};
        while (!que.empty()) {
            const auto& tmp = que.top();
            if (now.first != tmp.first) { break; } 
            if (tmp.second == 1) {
                plus += 1;
            } else {
                minus += 1;
            }
            que.pop();
        }
        ans += kind*plus + plus*(plus-1)/2;
        kind += plus - minus;
    }
    cout << ans;
}