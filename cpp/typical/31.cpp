#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vl = vector<long long>;
const int MOD = 998244353;

// 先手が勝つならtrue, 後手が勝つならfalse
bool solve(int w, int b, vector<vector<int>>& dp){
    if(dp[w][b] != -1) return dp[w][b];
    if(w == 0 && b < 2) return dp[w][b] = false;
    if (w >= 1 && !solve(w-1, b+w, dp)) return dp[w][b] = true;
    if (b >= 2) {
        for (int i = 1; i <= b/2; i++) {
            if (!solve(w, b-i, dp)) return dp[w][b] = true;
        }
    }
    return dp[w][b] = false;
}

int main(){
    int N;
    cin >> N;
    vector<int> W(N), B(N);
    for (int i = 0; i < N; i++) cin >> W[i];
    for (int i = 0; i < N; i++) cin >> B[i];

    vector<vector<int>> dp(51, vector<int>(50*50, -1));
    int win_first = 0;
    for (int i = 0; i < N; i++) {
        if (solve(W[i], B[i], dp)) {
            win_first++;
        }
    }
    cout << (win_first%2 == 1 ? "First" : "Second") << endl;

    for (const auto& x : dp | views::take(10)) {
        for (const auto& y : x | views::take(10)) {
            cout << y << " ";
        }
        cout << endl;
    }
}