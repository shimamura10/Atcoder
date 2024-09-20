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
    vector<pair<ll, int>> A(N);
    int sumZ = 0;
    for (int i=0; i<N; ++i) {
        ll x, y, z;
        cin >> x >> y >> z;
        int cost = max(0LL, (x+y)/2 - x + 1);
        A.emplace_back(cost, z);
        sumZ += z;
    }
    sort(A.begin(), A.end(), [](auto a, auto b){return a.first < b.first;});
    vl dp(sumZ+1, numeric_limits<ll>::max()/2);
    dp[0] = 0;
    for (const auto& [cost, z]: A) {
        for (int i=sumZ; i>=z; --i) {
            dp[i] = min(dp[i], dp[i-z] + cost);
        }
    }
    cout << *min_element(dp.begin()+(sumZ/2+1), dp.end())  << endl;
}