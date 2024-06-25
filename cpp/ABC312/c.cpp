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

int main(){
    int N, M;
    cin >> N >> M;
    vector<pair<char, int>> combine;
    for (int i=0; i<N; i++) {
        int a;
        cin >> a;
        combine.emplace_back('a', a);
    }
    for (int i=0; i<M; i++) {
        int b;
        cin >> b;
        combine.emplace_back('b', b);
    }

    sort(combine.begin(), combine.end(), [](const pair<char, int>& a, const pair<char, int>& b) {
        if (a.second == b.second)
            return a.first < b.first;
        return a.second < b.second;
    });

    int ans = 0;
    int cnt_sell = 0;
    int cnt_buy = M;
    for (const auto& c : combine) {
        if (c.first == 'a') {
            ans = c.second;
            cnt_sell++;
        } else {
            ans = c.second+1;
            cnt_buy--;
        }
        if (cnt_sell >= cnt_buy) {
            cout << ans << endl;
            return 0;
        }
    }
}