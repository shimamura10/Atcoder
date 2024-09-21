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
    int N, X, Y;
    cin >> N >> X >> Y;
    int MAX = 500000000;
    vector<vector<int>> dp(N+1, vector<int>(X+1, MAX));
    dp[0][0] = 0;
    for(int i = 0; i < N; i++){
        int A, B;
        cin >> A >> B;
        for(int j = i+1; j >= 1; j--){
            for (int k = X; k >= A; k--){
                dp[j][k] = min(dp[j][k], dp[j-1][k-A] + B);
            }
        }
    }
    int ans = 0;
    for (int j = 1; j <= N; j++){
        for (int k = 0; k <= X; k++){
            if (dp[j][k] <= Y){
                ans = max(ans, j);
            }
        }
    }
    if (ans < N) {
        ans++;
    }
    cout << ans << endl;
}