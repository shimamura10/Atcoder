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
    string S;
    cin >> S;
    vvi dp(S.size()+1, vi(S.size(), 0));
    dp[0][0] = 1;
    for (int i=0; i<S.size(); i++) {
        if (S[i] == '(') {
            for (int j=0; j<S.size()-1; j++) {
                if (dp[i][j] == 0) { continue; }
                dp[i+1][j+1] += dp[i][j];
                dp[i+1][j+1] %= MOD;
            }
        }
        if (S[i] == ')') {
            for (int j=1; j<S.size(); j++) {
                if (dp[i][j] == 0) { continue; }
                dp[i+1][j-1] += dp[i][j];
                dp[i+1][j-1] %= MOD;
            }
        }
        if (S[i] == '?') {
            for (int j=0; j<S.size(); j++) {
                if (dp[i][j] == 0) { continue; }
                dp[i+1][j+1] += dp[i][j];
                dp[i+1][j+1] %= MOD;
            }
            for (int j=1; j<S.size(); j++) {
                if (dp[i][j] == 0) { continue; }
                dp[i+1][j-1] += dp[i][j];
                dp[i+1][j-1] %= MOD;
            }
        }
    }
    cout << dp[S.size()][0] << endl;
}