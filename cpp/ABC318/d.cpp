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
    vector<vector<ll>> G(N, vector<ll>(N, 0));
    for (int i = 0; i < N-1; i++){
        for (int j = i+1; j < N; j++){
            cin >> G[i][j];
        }
    }

    vl dp(1<<N, 0);
    for (int bit = 0; bit < 1<<N; bit++) {
        int l = -1;
        for (int i = 0; i < N; i++) {
            if (!(bit>>i & 1)) {
                l = i;
                break;
            }
        }
        for (int j = l+1; j < N; j++) {
            if (!(bit>>j & 1)) {
                int nbit = bit | 1<<j | 1<<l;
                dp[nbit] = max(dp[nbit], dp[bit] + G[l][j]);
            }
        }
    }

    cout << dp[(1<<N)-1] << endl;

}