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

int main(){
    vector<ll> dp{9, 9};
    for (int i = 2; i < 38; i++) {
        dp.push_back(dp[i-2]*9LL + 9LL);
    }

    ll N;
    cin >> N;
    if (N == 1) {
        cout << 0 << endl;
        return 0;
    }
    N -= 1;
    for (int i = 0; i < 38; i++) {
        if (N <= dp[i]) {
            vi ans;
            while (i > 0) {
                auto tmp = dp[i]/9;
                ans.push_back(N/tmp);
                N %= tmp;
                i -= 2;
            }
            ans.push_back(N);
            for (int j = i/2; j>=0; j--) {
                ans.push_back(ans[j]);
            }
            for (int j = 0; j < ans.size(); j++) {
                cout << ans[j];
            }
            return 0;
        }
        N -= dp[i];
    }
}